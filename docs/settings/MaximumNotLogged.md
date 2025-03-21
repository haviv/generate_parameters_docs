# Maximum Not Logged

**Technical Name:** MaximumNotLogged

**Category:** Configuration

**Default Value:** 

**Impact Level:** Medium

**Description:**

The MaximumNotLogged parameter specifies the threshold for logging events within the Pathlock Cloud GRC platform. It determines the maximum duration or quantity of specific events that can occur without being logged, aiming to balance between operational efficiency and the need for oversight.

**Business Impact:**

Setting an appropriate MaximumNotLogged value ensures critical events are logged without overwhelming the system with trivial data. It aids in identifying potential security, risk, or compliance issues by capturing significant unlogged events. Misconfiguration could either lead to missing crucial data for audit and compliance purposes or to an excess of less relevant logs, impacting system performance and complicating analyses.

**Technical Impact when configured:**

- An optimized MaximumNotLogged setting enhances the platform's ability to log critical events while filtering out noise.
- Improves the system's performance by preventing an overload of the logging mechanism with inconsequential data.
- Ensures that significant events, which might indicate security or compliance issues, are captured and available for review.

**Examples Scenario:**

An organization configures MaximumNotLogged to ignore repetitive, inconsequential login attempts but captures and logs after a defined threshold of failed logins is reached. This configuration helps in identifying potential brute force attacks while not cluttering the log with every failed login attempt.

**Related Settings:** 

- CommonSettings.Default.Medium
- CommonSettings.Default.MediumLow

**Best Practices:** 

- Configure the MaximumNotLogged value according to the organizational needs for audit and compliance, ensuring critical events are not overlooked.
- Avoid setting the value too high to ensure that essential data is not missed.
- Regularly review and adjust the configuration as the organizational environment or priorities change.