# Show Transaction Application Area Column In Emergency Access

**Technical Name:** ShowTransactionApplicationAreaColumnInEmergancyAccess

**Category:** Reporting

**Default Value:** Not provided in the references

**Impact Level:** Medium

**Description:** This parameter controls the visibility of the Transaction Application Area column in reports related to Emergency Access activities within the Pathlock Cloud GRC platform. Enabling this feature will display an additional column, providing more detailed context around the transaction activities during emergency access scenarios.

**Business Impact:** Understanding the application area of transactions during emergency access is crucial for auditing and compliance purposes. It aids in the clear identification of potentially unauthorized or suspicious activities within specific application areas, thus enhancing the security posture and compliance reporting capabilities of the organization.

**Technical Impact when configured:** When enabled, reports generated for Emergency Access activities will include a column dedicated to showing the application areas of transactions. This allows for a more detailed analysis of the emergency access activities and helps in pinpointing specific areas within applications that are being accessed, which could be critical for security and audit reviews.

**Examples Scenario:** An organization needs to perform a detailed audit of emergency access granted to a high-privilege user account. Enabling the ShowTransactionApplicationAreaColumnInEmergancyAccess parameter will allow the audit team to see not only the transactions performed but also the application areas those transactions belong to, facilitating a thorough review and verification process against unauthorized or risky access.

**Related Settings:** ShowTransactionStatusColumn (Based on similarity in the code references and the context of showing additional information in reports.)

**Best Practices:** Configure when detailed auditing and review of emergency access activities are required, especially in highly regulated industries. Avoid when such details are unnecessary to minimize information overload in the reports.