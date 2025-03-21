# User Open Request Screen Show Add Info Button

**Technical Name:** UserOpenRequestScreenShowAddInfoButton

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**
This configuration parameter controls the visibility of the "Add Info" button on the User Open Request screen within the Pathlock Cloud GRC platform. When enabled, users have the ability to add additional information to their requests, enhancing the communication and documentation related to security or access requests.

**Business Impact:**
Enabling this button allows for a more interactive and transparent process for handling open requests. It facilitates a direct line of communication between requesters and approvers, potentially reducing the time to process requests by providing essential information upfront. This feature is particularly vital in scenarios where requests involve complex access rights or require detailed justification.

**Technical Impact when configured:**
- **Enabled:** The "Add Info" button becomes visible and functional on the User Open Request screen, allowing users to append additional information to their pending requests.
- **Disabled:** The button is hidden, and users won't have the option to provide extra details directly through the User Open Requests interface.

**Examples Scenario:**
An employee submits a request for elevated access rights to perform a critical task. The initial request does not provide enough context for the approvers to make an informed decision. With the "User Open Request Screen Show Add Info Button" enabled, the requester can easily add the necessary details, such as the reason for the request and the specific resources needed, thereby expediting the approval process.

**Related Settings:**
- ShowTransactionStatusColumn
- ShowTransactionApplicationAreaColumnInEmergancyAccess

**Best Practices:** 
- **Configure when:** There's a need for enhanced communication between requesters and approvers, or when requests frequently require additional context for decision-making.
- **Avoid when:** Requests are largely self-explanatory or additional information can be provided through other means, minimizing the need to complicate the request interface.