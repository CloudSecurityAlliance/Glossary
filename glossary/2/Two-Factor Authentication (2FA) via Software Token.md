# Two-Factor Authentication (2FA) via Software Token

A common two-factor authentication strategy is to have the user either generate a one time code on their end using a software token. The token software token simply generate a one time code that the user types in are vulnerable to phishing attacks.

There are newer software token software systems such as Google Smart Lock, Auth0 Guardian and Microsoft Authenticator that process the authentication request including information like the URL in the authentication request and it must be correct, an attacker can't simple use a similar looking domain to host their attack.

# Tags

Category:BlockchainAccountSecurityModel
Graph:Two-FactorAuthenticationviaSoftwareToken -->|defense against|PasswordTheft[Password Theft]
Graph:Two-FactorAuthenticationviaSoftwareToken -->|defense against|SimSWAP[Sim SWAP]
