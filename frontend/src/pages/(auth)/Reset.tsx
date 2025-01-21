
function ResetPasswordPage() {
  return (
    <div className="min-h-screen bg-gradient-to-r from-purple-500 to-pink-400 flex items-center justify-center">
      <div className="bg-white p-8 rounded-lg shadow-lg w-full max-w-md">
        {/* Header */}
        <h2 className="text-2xl font-bold text-gray-800 text-center">
          Reset Your Password
        </h2>
        <p className="text-gray-600 text-center mt-2">
          Enter your email to receive a password reset link.
        </p>

        {/* Form */}
        <form className="mt-6 space-y-4">
          {/* Email */}
          <div>
            <label className="block text-sm font-medium text-gray-700">
              Email Address
            </label>
            <input
              type="email"
              placeholder="Enter your email"
              className="mt-1 w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:ring-2 focus:ring-purple-500 focus:outline-none"
            />
          </div>

          {/* Submit Button */}
          <button
            type="submit"
            className="w-full bg-purple-500 text-white font-bold py-2 rounded-lg shadow-md hover:bg-purple-600 transition-colors duration-300"
          >
            Send Reset Link
          </button>
        </form>

        {/* Footer */}
        <div className="text-center text-gray-600 text-sm mt-6">
          <p>
            Remembered your password?{" "}
            <a
              href="/sign-in"
              className="text-purple-500 font-semibold hover:underline"
            >
              Sign In
            </a>
          </p>
          <p className="mt-2">
            Don’t have an account?{" "}
            <a
              href="/sign-up"
              className="text-pink-500 font-semibold hover:underline"
            >
              Sign Up
            </a>
          </p>
        </div>
      </div>
    </div>
  );
}

export default ResetPasswordPage;
