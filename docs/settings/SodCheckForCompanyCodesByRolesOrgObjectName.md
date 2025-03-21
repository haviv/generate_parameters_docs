**SoD Check For Company Codes By Roles Org Object Name**

**Technical Name:** SodCheckForCompanyCodesByRolesOrgObjectName

**Category:** SOD

**Default Value:**

**Impact Level:** High

**Description:**
The parameter `SodCheckForCompanyCodesByRolesOrgObjectName` enables the Pathlock Cloud GRC platform to evaluate the Segregation of Duties (SoD) risk by checking for company codes in role organization object names within the configured system landscape.

**Business Impact:**
Enabling this parameter ensures rigorous SoD checks, thus preventing unauthorized access and potential fraud within the company codes by scrutinizing roles and responsibilities. It ensures compliance with internal and external regulations concerning financial and operational integrity.

**Technical Impact when configured:**
Once configured, the system will perform advanced SoD checks by analyzing roles and permissions assigned to users, specifically focusing on company codes. This scrutiny helps in identifying high-risk authorizations and mitigating potential SoD violations.

**Examples Scenario:**
An organization has multiple roles defined in its ERP system with varying levels of access across different company codes. Enabling `SodCheckForCompanyCodesByRolesOrgObjectName` will help the compliance team to identify if a user has been granted roles that, collectively, could lead to a breach in SoD policies by having conflicting access within critical company codes.

**Related Settings:**

**Applicable Workflows Actions:**

**Best Practices:** configure when aiming to enhance SoD controls and compliance within your system. Avoid configuring if your SoD policy does not require strict oversight over company codes or if your organization operates with a single company code where such risks are minimal.