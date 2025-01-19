import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Layout from './pages/Layout'
import Home from './pages/Home'
import SignupPage from './pages/(auth)/Signup'
import SigninPage from './pages/(auth)/Signin'
import ResetPasswordPage from './pages/(auth)/Reset'
function App() {
  return (
    <>
    <Layout>

    <Router>
      <Routes>
        <Route path="/dashboard" element={<Home />} />
        <Route path='sign-in' element={<SigninPage />} />
        <Route path='sign-up' element={<SignupPage />} />
        <Route path='reset-password' element={<ResetPasswordPage />} />
      </Routes>
    </Router>
    </Layout>
    </>
  )
}

export default App
