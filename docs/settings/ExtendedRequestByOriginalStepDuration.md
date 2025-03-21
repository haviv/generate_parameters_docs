# Extended Request By Original Step Duration

**Technical Name:** ExtendedRequestByOriginalStepDuration

**Category:** Workflow

**Default Value:** N/A

**Impact Level:** Medium

**Description:**

This parameter is used to determine whether an extension request for emergency access steps within a workflow should be allowed based on the original step's duration. It is applicable in scenarios where emergency access involved in the workflow requires an extension beyond its initially allocated time.

**Business Impact:**

Enabling this parameter ensures that critical access required in emergency situations can be extended without re-initiating the entire access request process. This capability supports business continuity by allowing timely response to critical issues while ensuring that access governance policies are adhered to.

**Technical Impact when configured:**

When configured, this setting allows for dynamic adjustment of workflow steps related to emergency access (user creation, role assignment, etc.), ensuring users retain necessary permissions for the duration required to address the emergency. It directly impacts the efficiency and flexibility of managing emergency access within an organization's GRC policies.

**Example Scenario:**

A user is granted emergency access to a sensitive system due to an unplanned outage. Originally, the access was granted for 24 hours. However, resolving the issue is estimated to take an additional 12 hours. With ExtendedRequestByOriginalStepDuration enabled, the user's access can be extended without needing to undergo the access request workflow from the beginning, facilitating a faster resolution to the outage.

**Related Settings:**

- EnableProcessControlOpenRequestForDeleted

**Best Practices:** Configure when extended emergency access is a recurrent need within the organization to ensure swift action in critical situations. Avoid when stringent access duration policies are enforced, and extensions should be manually reviewed.