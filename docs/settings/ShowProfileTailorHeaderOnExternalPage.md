# Show Pathlock Header On External Page

**Technical Name:** ShowProfileTailorHeaderOnExternalPage

**Category:** General - UI

**Default Value:** 

**Impact Level:** Medium

**Description:**

Enables the display of the Pathlock header on external web pages. This feature is intended to promote consistency in the user interface and to ensure that platform branding is maintained across all external interfaces where Pathlock functionalities are accessed or embedded.

**Business Impact:**

The presence of the Pathlock header on external pages can enhance user trust and recognition of the platform, reassuring users that they are accessing official and secure Pathlock functionalities. This can be particularly impactful in environments where Pathlock is used extensively for governance, risk, and compliance (GRC) activities, ensuring that users feel secure and confident in their interactions with the platform, regardless of the context.

**Technical Impact when configured:**

When this parameter is configured to show the Pathlock header on external pages, any external web interface integrated with Pathlock will display the standardized header. This may include additional logos, navigation links, or access controls provided by Pathlock, depending on the platform's customization settings.

**Examples Scenario:**

A company uses Pathlock for their GRC activities and has developed an external portal for managers to review and manage compliance reports. Enabling this parameter would ensure that when managers access this external portal, the Pathlock header is displayed, creating a seamless user experience that aligns with the internal Pathlock platform interface.

**Related Settings:** 

- ShowIsApprovedOnPageStart
- ShowEventDetailsInWorkflow

**Best Practices:** configure when an external interface requires brand consistency and user reassurance; avoid when external interfaces demand a distinct appearance or when limiting Pathlock's visibility is strategically desired.