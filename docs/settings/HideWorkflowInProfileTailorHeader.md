# Hide Workflow In Pathlock Header

**Technical Name:** HideWorkflowInProfileTailorHeader

**Category:** Configuration

**Default Value:** Not specified

**Impact Level:** Medium

**Description:**

The HideWorkflowInProfileTailorHeader parameter is designed to control the visibility of workflow-related information within the Pathlock platform's header section. This configuration is particularly relevant in the context of the ProfileTailor application, aiming to provide a cleaner, more focused user interface by optionally concealing workflow initiation points or status indicators from the main application header.

**Business Impact:**

Configuring this parameter can directly impact how users interact with workflows within the Pathlock platform. By hiding workflow-related elements, organizations can streamline the user interface, reducing potential distractions and focusing user activities on more critical areas of compliance, risk management, or security oversight. This setting can be particularly beneficial in scenarios where workflow functionalities are not central to the user's daily tasks or where a simplified UI can enhance operational efficiency.

**Technical Impact when configured:**

Upon activation, this setting will prevent the display of any workflow-related options, buttons, or notifications within the ProfileTailor application's header. This could include options to initiate new workflows, check the status of ongoing ones, or receive alerts about workflow outcomes. As a result, users may need to access these functions through alternative navigation paths within the application.

**Examples Scenario:**

In a scenario where an organization seeks to deploy the Pathlock platform primarily for compliance monitoring and risk assessment, rather than for detailed workflow management, the HideWorkflowInProfileTailorHeader parameter can be enabled to offer a cleaner interface to users. This ensures that users are not overwhelmed by workflow options that are peripheral to their main tasks, thus enhancing usability and focus on compliance activities.

**Related Settings:** Not specified

**Best Practices:** 

- **Configure when:** The focus is on streamlining the user interface for roles or scenarios where workflow management is not a primary function. Configuring this parameter can reduce clutter and enhance the user experience for specific user groups within the Pathlock platform.
  
- **Avoid when:** Workflow management features are central to the user's daily operations within the Pathlock platform. Hiding these options could hinder their ability to manage and participate in workflows efficiently.