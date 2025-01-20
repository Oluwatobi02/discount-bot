import { useEffect, useState } from "react";
import { router } from "@/main";
import emitter from "@/lib/emitter";

export default function Navbar() {
  const [isSignedIn, setIsSignedIn] = useState(false);

  const handleNavigate = (link: string) => {
    router.navigate(link);
  };

  useEffect(() => {
    const handleLogin = () => setIsSignedIn(true);
    const handleLogout = () => setIsSignedIn(false);

    emitter.on("login", handleLogin);
    emitter.on("logout", handleLogout);

    return () => {
      emitter.off("login", handleLogin);
      emitter.off("logout", handleLogout);
    };
  }, []);

  return (
    <nav className="w-full bg-gradient-to-r from-blue-500 to-teal-400 shadow-md">
      <div className="max-w-7xl mx-auto px-6 sm:px-8 lg:px-10 py-4 flex items-center justify-between">
        {/* Logo */}
        <div
          className="text-2xl font-bold text-white cursor-pointer select-none 
          tracking-widest transition-transform duration-300 transform hover:scale-105"
          onClick={() => handleNavigate("/")}
        >
          Price<span className="text-teal-200">Tracker</span>
        </div>

        {/* Avatar or Sign In/Up */}
        <div className="relative">
          {isSignedIn ? (
            <div
              className="w-10 h-10 bg-cover bg-center rounded-full border-4 border-white shadow-md 
              transition-all duration-300 transform hover:scale-110 hover:shadow-lg"
              style={{
                backgroundImage:
                  "url('https://www.w3schools.com/w3images/avatar2.png')",
              }}
              onClick={() => console.log("Avatar clicked!")}
            ></div>
          ) : (
            <div className="flex space-x-4">
              <button
                className="text-sm px-5 py-2 rounded-md bg-white text-blue-500 font-semibold 
                hover:bg-teal-200 transition-all duration-300 shadow-sm"
                onClick={() => handleNavigate("/sign-in")}
              >
                Sign In
              </button>
              <button
                className="text-sm px-5 py-2 rounded-md bg-teal-500 text-white font-semibold 
                hover:bg-teal-600 transition-all duration-300 shadow-sm"
                onClick={() => handleNavigate("/sign-up")}
              >
                Sign Up
              </button>
            </div>
          )}
        </div>
      </div>
    </nav>
  );
}
