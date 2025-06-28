import base64

credentials = "sfuser@SFPRO002764:MyPassword:Lms2025%"
print(base64.b64encode(credentials.encode()).decode())
