async function testFetch() {
    const token = "eyJ0b2tlbkNvbnRlbnQiOnsiYXBpS2V5IjoiWlRWbU0yRXpZMk5pTnpaallXVTRaRFppTkRobE0yUm1ZelUzWXciLCJzZlByaW5jaXBsZSI6InNmYWRtaW4jRElWI1NGUFJPMDAyNzY0IiwiaXNzdWVkRm9yIjoiQVBJVEVTVCIsInNjb3BlIjoiIiwiaXNzdWVkQXQiOjE3NDE1ODYyMjk5MTcsImV4cGlyZXNBdCI6MTc0MTY3MjYyOTkxN30sInNpZ25hdHVyZSI6Im9xUTRkdXN2OHJJVW85ZzlScnRKWXFDcGMyRCtJZ0JOV3BCUWJERkQwWGt0Wk0wL0UwSjBicGFqVWhUZE1oWmI4dVlONWVYelg3enh0UFNPWm8yeXVTZXVGSitIdWJ3RS9pWkdyMk5PZmx3Wi9UMyswblNYLzltbi9jbXhvQWE2Yk40NjVoUzNuaGJ2OTNrVzR4dW9iYTJvT3RMUVBic3JFNWR3L3MvSTdmVT0ifQ=="; // Use your actual token
    const apiUrl = "https://apisalesdemo8.successfactors.com/odata/v2/EmpEmployment(personIdExternal='sfadmin',userId='sfadmin')/jobInfoNav";

    try {
        const response = await fetch(apiUrl, {
            method: "GET",
            headers: {
                "Authorization": `Bearer ${token}`,
                "Accept": "application/json"
            }
        });

        if (!response.ok) {
            throw new Error(`Error: ${response.status} - ${await response.text()}`);
        }

        const data = await response.json();
        console.log("SuccessFactors Data:", data);
    } catch (error) {
        console.error("Failed to fetch:", error);
    }
}

testFetch();
