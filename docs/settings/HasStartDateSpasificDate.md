# Display default value for start date:

**Technical Name:** HasStartDateSpasificDate

**Category:** Configuration

**Default Value:** Not applicable

**Impact Level:** Medium

**Description:**

The `HasStartDateSpasificDate` parameter is designed to specify whether a specific start date is set for accessing a feature or workflow within the Pathlock Cloud GRC platform. This parameter is crucial for ensuring that certain actions or features are only available after a specified date, contributing to the structured rollout of features or compliance initiatives.

**Business Impact:**

Setting this parameter helps organizations plan and control the deployment of new features, compliance requirements, or any changes in the workflow that need to be introduced gradually or at a specific time. It ensures that users are only able to access or perform certain actions after the designated start date, aiding in better change management and adherence to compliance schedules.

**Technical Impact when configured:**

When configured, the parameter restricts access to certain features or parts of the application until the specified start date is reached. This can be used to manage feature rollouts, compliance deadlines, or to align the application's capabilities with the organization's internal schedule or external regulatory requirements.

**Example Scenario:**

An organization is planning to roll out a new compliance process in the Pathlock Cloud GRC platform that should only be accessible starting from the next financial quarter. By using the `HasStartDateSpasificDate` parameter, they can set up the system so that the compliance process becomes automatically available to users only when the specified date is reached, facilitating a smooth transition and ensuring no early access.

**Related Settings:** 

- `FormatedQuarterPattern`: Might be involved when the start date relates to fiscal quarters.
- `EventsDetailsTableText`: Could be relevant if the start date impacts when certain events or summaries are emailed or made accessible.

**Applicable Workflows Actions:** 

This attribute is not applicable as no specific workflow actions were identified in the provided context.

**Best Practices:** 

- **Configure when:** There is a need to control the availability of features, workflows, or compliance processes based on specific dates.
- **Avoid when:** Immediate access to features or functionalities is necessary, or if the feature/workflow should be available to all users without date restrictions.