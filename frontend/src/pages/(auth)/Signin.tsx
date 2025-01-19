import { login, signup } from "@/lib/utils";
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

function SigninPage() {
  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });
const navigate = useNavigate()
  const handleInputChange = (e: React.FormEvent) => {
    const { name, value } = e.target as HTMLInputElement;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    // Pass formData to your sign-in function
    console.log("Form Data Submitted:", formData);
    // Add your sign-in logic here
    const res = await login(formData)
    if (res.success) {
      sessionStorage.setItem("user", res.data.user._id);
      console.log("Login Successful:", res);
      navigate("/dashboard");
    } else {
      console.error("Login Error:", res.error);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-r from-blue-500 to-teal-400 flex items-center justify-center">
      <div className="bg-white p-8 rounded-lg shadow-lg w-full max-w-md">
        {/* Header */}
        <h2 className="text-2xl font-bold text-gray-800 text-center">
          Welcome Back!
        </h2>
        <p className="text-gray-600 text-center mt-2">
          Sign in to access your account.
        </p>

        {/* Form */}
        <form className="mt-6 space-y-4" onSubmit={handleSubmit}>
          {/* Email */}
          <div>
            <label className="block text-sm font-medium text-gray-700">
              Email Address
            </label>
            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleInputChange}
              placeholder="Enter your email"
              className="mt-1 w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:ring-2 focus:ring-blue-500 focus:outline-none"
            />
          </div>

          {/* Password */}
          <div>
            <label className="block text-sm font-medium text-gray-700">
              Password
            </label>
            <input
              type="password"
              name="password"
              value={formData.password}
              onChange={handleInputChange}
              placeholder="Enter your password"
              className="mt-1 w-full px-4 py-2 border border-gray-300 rounded-lg shadow-sm focus:ring-2 focus:ring-blue-500 focus:outline-none"
            />
          </div>

          {/* Submit Button */}
          <button
            type="submit"
            className="w-full bg-blue-500 text-white font-bold py-2 rounded-lg shadow-md hover:bg-blue-600 transition-colors duration-300"
          >
            Sign In
          </button>
        </form>

        {/* Footer */}
        <div className="text-center text-gray-600 text-sm mt-6">
          <p>
            Forgot your password?{" "}
            <a
              href="/reset-password"
              className="text-blue-500 font-semibold hover:underline"
            >
              Reset it here
            </a>
          </p>
          <p className="mt-2">
            Don’t have an account?{" "}
            <a
              href="/sign-up"
              className="text-teal-500 font-semibold hover:underline"
            >
              Sign Up
            </a>
          </p>
        </div>
      </div>
    </div>
  );
}

export default SigninPage;
