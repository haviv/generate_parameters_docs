# Campaigns Review Details Tab SoD Roles

**Technical Name:** CampaignsReviewDetailsTabSODRoles

**Category:** SOD

**Default Value:**

**Impact Level:** High

**Description:** This parameter configures the visibility and functionality of Segregation of Duties (SoD) roles within the Campaigns Review Details tab. It is crucial for managing risk associated with conflicting roles and ensuring compliance with internal and external audit requirements.

**Business Impact:** Proper configuration helps prevent fraud and errors by ensuring that sensitive tasks are separated among different roles. This supports compliance with regulatory requirements and internal control principles, thereby reducing the risk of non-compliance penalties and reputational damage.

**Technical Impact when configured:** Determines the inclusion and management of SoD roles information within authorization certification details, enhancing the oversight and control over access rights and segregation duties within the system.

**Examples Scenario:** If an organization requires strict adherence to internal controls where a single individual should not perform conflicting tasks, enabling this parameter would enforce the visibility and management of SoD roles to prevent unauthorized access combinations within certification campaigns.

**Related Settings:** 
- CampaignsReviewDetailsTabUARHistory
- CampaignsReviewDetailsTabUARPeerAnalysis

**Best Practices:** 
- **Configure when:** Implementing or reviewing internal controls and compliance requirements related to access management and segregation of duties within your GRC framework.
- **Avoid when:** There are no strict requirements for segregation of duties or when the organization operates in a highly trust-based environment with less stringent internal controls. However, caution is advised given the high impact on compliance and risk management.