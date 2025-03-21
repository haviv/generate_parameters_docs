# Active Directory Provider Additional Fields

**Technical Name:** ActiveDirectoryProviderAdditionalFields

**Category:** User Management

**Default Value:** 

**Impact Level:** Medium

**Description:**

This parameter allows for the specification of additional fields from the Active Directory to be included during the synchronization process into the Pathlock Cloud GRC platform's organization structure. It is used primarily in the context of importing user details and attributes in a more granular and customized manner than what is offered by default.

**Business Impact:**

Inclusion of these additional fields can significantly enhance the organization's ability to tailor the GRC platform's user management functionalities to align with existing Active Directory schemas and to ensure a more comprehensive and detailed user profile is available for GRC processes. This can impact areas such as access control, reporting, and compliance auditing by providing more detailed user information.

**Technical Impact when configured:**

Upon configuration, the system will query and import the specified Active Directory fields into the Pathlock Cloud GRC platform during each synchronization cycle. This allows for extended attributes, that are not part of the standard sync, to be utilized for enhanced user profiling, detailed reporting, and precise access and compliance management.

**Examples Scenario:**

Assuming an organization wants to include an employee identification number (EIN) and department name that aren't part of the standard Active Directory fields synchronized by the Pathlock Cloud GRC platform. By configuring the ActiveDirectoryProviderAdditionalFields parameter to include these specific fields, the organization can ensure this information is imported into the platform, allowing for more detailed reporting and user management based on EINs and department names.

**Related Settings:**
- SoDReviewEveryMonths

**Best Practices:** 

- **Configure when:**
  - Detailed user information needs to be part of the GRC platform for compliance, risk management, or to enhance security protocols.
  - Custom user attributes present within the Active Directory need to be leveraged within the GRC processes.
- **Avoid when:**
  - The inclusion of additional information does not provide tangible benefits to the GRC processes or could potentially lead to data overload.
  - There are concerns regarding the privacy and security of importing specific additional fields from the Active Directory.