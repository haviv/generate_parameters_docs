# Password Recover Minutes Wait Before Reset Last Login

**Technical Name:** PasswordRecover_MinutesWaitBeforeResetLastLogin

**Category:** User Management

**Default Value:** 

**Impact Level:** Medium

**Description:**

This parameter defines the minimum waiting period, in minutes, before the last login attempt counter is reset for a user attempting to recover their password. It is designed to enhance security by preventing rapid, repeated password recovery attempts, which could indicate brute force attacks.

**Business Impact:**

Setting an appropriate waiting period helps in mitigating the risk of unauthorized access through automated password recovery attempts. It strikes a balance between security and user convenience by ensuring users are not permanently or excessively locked out of their accounts while still protecting against potential security breaches.

**Technical Impact when configured:**

When configured correctly, this setting will delay subsequent attempts to recover passwords, thereby reducing the risk of unauthorized access through brute force methods. It directly impacts user experience by imposing a waiting period after a defined number of unsuccessful login attempts.

**Examples Scenario:**

For example, if this parameter is set to 5 minutes, a user who fails to successfully recover their password must wait for 5 minutes before the system resets the last login attempt counter, allowing them to try again.

**Related Settings:** 

- PasswordRecover_MaximumLoginAttempts

**Best Practices:** configure when

- You have identified a need to secure user accounts against brute force attacks further.
- Your organization operates in regions or sectors with stringent regulatory requirements regarding account access and security. 

avoid when 

- Users require immediate re-attempts for password recovery due to business needs, and alternative security measures are in place.
