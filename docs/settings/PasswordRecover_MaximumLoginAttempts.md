# Password Recover Maximum Login Attempts

**Technical Name:** PasswordRecover_MaximumLoginAttempts

**Category:** Security

**Default Value:**

**Impact Level:** High

**Description:**

The `PasswordRecover_MaximumLoginAttempts` parameter defines the maximum number of login attempts a user can make when trying to recover their password through the Pathlock Cloud GRC platform. This setting helps protect against brute force attacks aiming to guess or crack passwords.

**Business Impact:**

Implementing a limit on login attempts for password recovery enhances the security posture of an organization by minimizing the risk of unauthorized access. It prevents attackers from using automated tools to guess passwords, thereby safeguarding sensitive GRC data and compliance-related information.

**Technical Impact when configured:**

Configuring this parameter to a strict, but reasonable number of attempts, significantly reduces the risk of account compromise while ensuring legitimate users can recover their passwords without undue hassle.

**Examples Scenario:**

- **Scenario 1:** If the `PasswordRecover_MaximumLoginAttempts` is set too low, legitimate users might get locked out of their accounts accidentally, possibly impacting their work and productivity.
- **Scenario 2:** If set too high, it might offer attackers more chances to guess user passwords, increasing the risk of unauthorized access.

**Related Settings:**

- `AccountLockoutThreshold`
- `AccountLockoutDuration`

**Best Practices:** 

- **Configure when:** You have assessed the user behavior within your organization and understand the average attempts needed for successful password recovery. Adjust the setting to slightly above this average to accommodate legitimate users while keeping security tight.
- **Avoid when:** Setting an extremely high value that could make brute force attacks feasible or setting it too low, which may result in increased support calls due to users being locked out of their accounts.