**Locked By Incorrect Logons Code**

**Technical Name:** LockedByIncorrectLogonsCode

**Category:** Security

**Default Value:**

**Impact Level:** High

**Description:**

The Locked By Incorrect Logons Code parameter is a security feature within the Pathlock Cloud GRC platform that determines the protocol to follow when a user account has been locked due to multiple incorrect login attempts. This parameter ensures that user accounts are safeguarded against unauthorized access attempts, enhancing the overall security posture of the organization.

**Business Impact:**

Implementing this parameter effectively reduces the risk of security breaches by preventing attackers from gaining access through brute force attacks. It also promotes a culture of security awareness among users, encouraging them to safeguard their credentials diligently.

**Technical Impact when configured:**

When configured, this parameter activates account lockouts after a predetermined number of incorrect login attempts. It impacts system accessibility for the affected user accounts, requiring administrative intervention or a predefined timeout period before the account is unlocked. This mechanism helps to protect sensitive company data by restricting access after suspicious login activities.

**Examples Scenario:**

- **Scenario:** An attacker attempting to gain unauthorized access to a high-privileged user account by trying multiple password combinations.
  - **Without 'Locked By Incorrect Logons Code':** The attacker might eventually guess the correct password, gaining unauthorized access.
  - **With 'Locked By Incorrect Logons Code' Activated:** The account is locked after a few incorrect attempts, preventing unauthorized access and alerting administrators to the potential attack.

**Related Settings:**

- ProfileTailorContext.Context.SystemCode
- User.SystemId

**Best Practices:** configure when high-security measures are necessary, avoid when user convenience is a higher priority and the risk of attack is considered low.