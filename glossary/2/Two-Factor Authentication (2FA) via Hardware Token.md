# Two-Factor Authentication (2FA) via Hardware Token

A common two-factor authentication strategy is to have the user either generate a one time code on their end using a hardware token such as an RSA token, or a U2F/FIDO compliant hardware token such as a Yubikey or a Google Titan key. The token that simply generate a one time code that the user types in are vulnerable to phishing attacks, however the hardware tokens implementing protocols such as U2F are more secure as they include the URL in the authentication request and it must be correct, an attacker can't simple use a similar looking domain to host their attack.

# Tags

Category:BlockchainAccountSecurityModel
Category:BlockchainSecurity
Graph:Two-FactorAuthenticationviaHardwareToken -->|defense against|PasswordTheftAttack[Password Theft Attack]
Graph:Two-FactorAuthenticationviaHardwareToken -->|defense against|SimSWAP[Sim SWAP]
