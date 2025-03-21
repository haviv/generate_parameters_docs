# User Open Request Screen Show End Request Button

**Technical Name:** UserOpenRequestScreenShowEndRequestButton

**Category:** Workflow

**Default Value:** True (inferred based on typical behavior; explicit default value not provided in the referenced code)

**Impact Level:** Medium

**Description:**

This parameter controls the visibility of the "End Request" button on the User Open Request Screen within the Pathlock Cloud GRC platform. When enabled, the button is visible, allowing users to end or close their open requests directly from the screen.

**Business Impact:**

Enabling this feature enhances user autonomy by allowing them to directly manage the lifecycle of their requests without needing to wait for administrative action. This can lead to improved workflow efficiency and user satisfaction. However, it also requires that the users are well-informed about the implications of ending a request to avoid premature closure that could disrupt established processes.

**Technical Impact when configured:**

When enabled, the "End Request" option becomes available for user-initiated actions in their open requests workflow view. This enables quicker resolutions and user empowerment but should be managed carefully to ensure that it aligns with business processes and audit requirements.

**Examples Scenario:**

- **Scenario:** A user, after initiating a request for access to a particular system, realizes they no longer need the access due to a change in project scope. With this feature enabled, they can directly end the request, saving time for both themselves and the approvers.
  
- **Scenario:** An organization implements a policy that certain types of requests, such as those for temporary elevated access, can be withdrawn by the requester if they complete their tasks earlier than anticipated. This setting enables compliance with the policy by providing the necessary UI element.

**Related Settings:** None explicitly mentioned, but likely related to settings that control workflow UI elements and permissions.

**Best Practices:** 

- **Configure when:** Users are knowledgeable about their workflows and can responsibly manage their requests. In environments where rapid processing of requests and user autonomy are prioritized.
  
- **Avoid when:** The premature ending of requests could lead to compliance issues, or where there is a risk of users inadvertently disrupting workflow steps. In such cases, it’s better managed through a process that requires approver intervention.