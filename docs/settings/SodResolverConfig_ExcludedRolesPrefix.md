**SoD Resolver Config Excluded Roles Prefix**

**Technical Name:** SodResolverConfig_ExcludedRolesPrefix

**Category:** Configuration

**Default Value:** (The default value was not provided in the code references.)

**Impact Level:** Medium

**Description:** This parameter specifies a prefix used to exclude certain roles from Separation of Duties (SoD) violation checks within the Pathlock Cloud GRC platform. The specified prefix helps in filtering out roles that should not be considered during SoD analysis, ensuring more focused and relevant compliance results.

**Business Impact:** Fine-tuning the SoD analysis by excluding specific roles can significantly enhance the efficiency and accuracy of compliance reporting. It enables organizations to tailor the compliance checks to their unique operational context, reducing false positives and focusing on the roles that are critical for security and compliance.

**Technical Impact when configured:** When configured, the system will automatically bypass any roles with the specified prefix during SoD violation checks. This ensures that roles intended for administrative purposes, testing, or other non-sensitive functions do not trigger unnecessary SoD alerts, streamlining the compliance management process.

**Example Scenario:** 

- **Situation:** A company has a series of roles prefixed with "TEST_" that are used solely for testing purposes and should not be considered during SoD checks.
  
- **Action:** By configuring the `SodResolverConfig_ExcludedRolesPrefix` parameter with the prefix "TEST_", those roles will be excluded from SoD violation analyses.
  
- **Outcome:** The exclusion of test roles simplifies the SoD reports, focusing only on actual user roles that impact the company's security and compliance posture.

**Related Settings:** 

- `SodCheckForCompanyCodesByRoles`

**Best Practices:** Configure this parameter when you have specific roles that consistently do not require SoD checks, such as test, demo, or administrative roles. Avoid using it in a way that could inadvertently exclude roles that should be subject to compliance checks.