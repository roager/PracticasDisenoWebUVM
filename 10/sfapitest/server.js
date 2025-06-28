const express = require("express");
const cors = require("cors");

const app = express();
const PORT = 3000;

app.use(express.json());
app.use(cors());

const token = "eyJ0b2tlbkNvbnRlbnQiOnsiYXBpS2V5IjoiWlRWbU0yRXpZMk5pTnpaallXVTRaRFppTkRobE0yUm1ZelUzWXciLCJzZlByaW5jaXBsZSI6InNmYWRtaW4jRElWI1NGUFJPMDAyNzY0IiwiaXNzdWVkRm9yIjoiQVBJVEVTVCIsInNjb3BlIjoiIiwiaXNzdWVkQXQiOjE3NDE1ODYyMjk5MTcsImV4cGlyZXNBdCI6MTc0MTY3MjYyOTkxN30sInNpZ25hdHVyZSI6Im9xUTRkdXN2OHJJVW85ZzlScnRKWXFDcGMyRCtJZ0JOV3BCUWJERkQwWGt0Wk0wL0UwSjBicGFqVWhUZE1oWmI4dVlONWVYelg3enh0UFNPWm8yeXVTZXVGSitIdWJ3RS9pWkdyMk5PZmx3Wi9UMyswblNYLzltbi9jbXhvQWE2Yk40NjVoUzNuaGJ2OTNrVzR4dW9iYTJvT3RMUVBic3JFNWR3L3MvSTdmVT0ifQ=="; // ✅ Use the same token as Postman

app.get("/fetch-employee", async (req, res) => {
    const personId = req.query.personId;
    if (!personId) {
        return res.status(400).json({ error: "Missing personIdExternal" });
    }

    const apiUrl = `https://apisalesdemo8.successfactors.com/odata/v2/EmpEmployment(personIdExternal='${personId}',userId='${personId}')/jobInfoNav`;

    try {
        console.log(`Fetching data for: ${personId}`);
        const response = await fetch(apiUrl, {
            method: "GET",
            headers: {
                "Authorization": `Bearer ${token}`, // ✅ Matches Postman
                "Accept": "application/json"        // ✅ Matches Postman
            }
        });

        console.log(`Response status: ${response.status}`);

        if (!response.ok) {
            const errorText = await response.text();
            console.error(`Error response from API: ${errorText}`);
            return res.status(response.status).json({ error: errorText });
        }

        const data = await response.json();
        console.log("Data fetched successfully:", data);
        res.json(data);
    } catch (error) {
        console.error("Server Error:", error);
        res.status(500).json({ error: error.message });
    }
});

app.listen(PORT, "127.0.0.1", () => {
    console.log(`Server running on http://127.0.0.1:${PORT}`);
});

