```mermaid
graph LR
BlockchainAccountSecurityModel(BlockchainAccountSecurityModel)
Phishing -->|results in|PasswordTheftAttack[Password Theft Attack]
SimSWAP -->|attack against|Two-FactorAuthenticationviaPhoneCall[Two-Factor Authentication 2FA via Phone Call]
SimSWAP -->|attack against|Two-FactorAuthenticationviaSMS[Two-Factor Authentication 2FA via SMS]
Two-FactorAuthentication -->|defense against|PasswordTheft[Password Theft]
Two-FactorAuthenticationviaBiometrics -->|defense against|PasswordTheft[Password Theft]
Two-FactorAuthenticationviaBiometrics -->|defense against|SimSWAP[Sim SWAP]
Two-FactorAuthenticationviaEmail -->|defense against|PasswordTheft[Password Theft]
Two-FactorAuthenticationviaEmail -->|defense against|SimSWAP[Sim SWAP]
Two-FactorAuthenticationviaHardwareToken -->|defense against|PasswordTheft[Password Theft]
Two-FactorAuthenticationviaHardwareToken -->|defense against|SimSWAP[Sim SWAP]
Two-FactorAuthenticationviaOneTimeCode -->|defense against|PasswordTheft[Password Theft]
Two-FactorAuthenticationviaPhoneCall -->|defense against|PasswordTheft[Password Theft]
Two-FactorAuthenticationviaPhysicalMail -->|defense against|PasswordTheft[Password Theft]
Two-FactorAuthenticationviaSMS -->|defense against|PasswordTheft[Password Theft]
Two-FactorAuthenticationviaSoftwareToken -->|defense against|PasswordTheft[Password Theft]
Two-FactorAuthenticationviaSoftwareToken -->|defense against|SimSWAP[Sim SWAP]
