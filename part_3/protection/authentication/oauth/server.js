require('dotenv').config();
const express = require('express');
const axios = require('axios');
const session = require('express-session');

const app = express();
const { PORT, SESSION_SECRET, GITHUB_CLIENT_ID, GITHUB_CLIENT_SECRET, GITHUB_CALLBACK } = process.env;

app.use(session({ secret: SESSION_SECRET, resave: false, saveUninitialized: false }));
app.use(express.json());

// Página de inicio
app.get('/', (req, res) => {
  res.send(`
    <h1>OAuth Demo Lautaorsi</h1>
    <p>${req.session.user ? `Registrado como <b>${req.session.user.login}</b>` : 'No registrado'}</p>
    <ul>
      <li><a href="/login">Iniciar sesión con GitHub</a></li>
      <li><a href="/api/hello_protected">GET /api/hello_protected (protegido)</a></li>
      <li><a href="/api/hello_unprotected">GET /api/hello_unprotected (no protegido)</a></li>
      <li><a href="/logout">Cerrar sesión</a></li>
    </ul>
  `);
});

// Redirección a mi github
app.get('/login', (req, res) => {
  const params = new URLSearchParams({
    client_id: GITHUB_CLIENT_ID,
    redirect_uri: GITHUB_CALLBACK,
    scope: 'read:user user:email'
  });
  res.redirect(`https://github.com/login/oauth/authorize?${params.toString()}`);
});

// Vuelta desde github a página
app.get('/callback', async (req, res) => {
  const { code } = req.query;
  if (!code) return res.status(400).send('Missing code');

  try {
    // Obtener token pasado por Github
    const tokenRes = await axios.post(
      'https://github.com/login/oauth/access_token',
      {
        client_id: GITHUB_CLIENT_ID,
        client_secret: GITHUB_CLIENT_SECRET,
        code,
        redirect_uri: GITHUB_CALLBACK
      },
      { headers: { Accept: 'application/json' } }
    );

    const access_token = tokenRes.data.access_token;
    if (!access_token) return res.status(401).send('Token exchange failed');

    // Obtenemos perfil de usuario
    const userRes = await axios.get('https://api.github.com/user', {
      headers: { Authorization: `Bearer ${access_token}`, Accept: 'application/json' }
    });

    // Guardamos datos del usuario (nombre y mail)
    req.session.user = { login: userRes.data.login, id: userRes.data.id };
    res.redirect('/');
  } catch (err) {
    console.error('OAuth error:', err.response?.data || err.message);
    res.status(500).send('OAuth error. Check terminal for details.');
  }
});

// Verificación de permisos para la ruta protegida
function requireAuth(req, res, next) {
  if (req.session.user) return next();
  res.status(401).json({ error: 'Unauthorized. Visit /login first.' });
}

// endpoint hello protegido, usa requireAuth antes de handlear la request.
app.get('/api/hello_protected', requireAuth, (req, res) => {
  res.json({ message: `Hola ${req.session.user.login}!` });
});


// endpoint hello no protegido, no usa requireAuth antes de handlear la request.
app.get('/api/hello_unprotected', (req, res) => {
  res.json({ message: `Hola, no se quién sos!` });
});

// Logout
app.get('/logout', (req, res) => {
  req.session.destroy(() => res.redirect('/'));
});

app.listen(PORT, () => console.log(`Running on http://localhost:${PORT}`));