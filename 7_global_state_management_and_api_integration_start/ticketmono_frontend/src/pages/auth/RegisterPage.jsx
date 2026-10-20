import { useAuth } from "../../hooks/useAuth"

function RegisterPage() {
  const { register, isRegistering, registerError } = useAuth()

  function handleRegistration(formData) {
      register(formData, {
        onSuccess: () => {
          // navigate('/login')
        }
      })
  }

  return (
    <div>
      <h1 className="text-2xl font-bold">Register Page</h1>
    </div>
  )
}

export default RegisterPage
