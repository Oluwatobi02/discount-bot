// const url = `https://projectspace.tech'
const url = 'http://backend:5000'
export const productFetcher = async(page: Number, user_id: string='') => {
    try {
        const response = await fetch(`${url}/products?page=${page}`,
        {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'userid': user_id
            }
        }
        )
        return await response.json()

    } catch (error) {
        console.error(error)
    }

}

export const signup = async (userData: { name: string; email: string; phone: string; password: string }) => {
    try {
      const response = await fetch(`${url}/sign-up`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(userData),
      });
  
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.message || "Failed to sign up. Please try again.");
      }
  
      const data = await response.json();
      return { success: true, data }; // Return success response
    } catch (error) {
      console.error("Signup Error:", error);
      return { success: false, error }; // Return error response
    }
  };
  
  export const login = async (credentials: { email: string; password: string }) => {
    try {
      const response = await fetch(`${url}/login`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(credentials),
      });
  
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.message || "Invalid email or password.");
      }
  
      const data = await response.json();
      return { success: true, data }; // Return success response
    } catch (error) {
      console.error("Login Error:", error);
      return { success: false, error }; // Return error response
    }
  };
  

export async function watchProduct(productId: string) {
  const userId = sessionStorage.getItem("user");
  if (!userId) return { success: false, error: new Error("User not logged in.") };
    try {
        const response = await fetch(`${url}/products/${productId}/watch`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                "user": userId
            }
        })
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.message || "Failed to watch product. Please try again.");
        }
        const data = await response.json();
        return { success: true, data };
    }
    catch (error) {
        console.error("Watch Product Error:", error);
        return { success: false, error };
    }
}
export async function unWatchProduct(productId: string) {
  const userId = sessionStorage.getItem("user");
  if (!userId) return { success: false, error: new Error("User not logged in.") };
    try {
        const response = await fetch(`${url}/products/${productId}/unwatch`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                "user": userId
            }
        })
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.message || "Failed to watch product. Please try again.");
        }
        const data = await response.json();
        return { success: true, data };
    }
    catch (error) {
        console.error("Watch Product Error:", error);
        return { success: false, error };
    }
}