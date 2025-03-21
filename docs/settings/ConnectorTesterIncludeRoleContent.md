# Connector Tester Include Role Content

**Technical Name:** ConnectorTesterIncludeRoleContent

**Category:** Configuration

**Default Value:** False

**Impact Level:** Medium

**Description:**

This parameter controls whether role content details are included in the connector testing process within the Pathlock Cloud GRC platform. When enabled, it ensures comprehensive testing of connectors by including role-related content in the test scenarios.

**Business Impact:**

Enabling this feature ensures more thorough testing which can identify potential issues with role content that may affect security, compliance, and the effective management of access rights within the organization. It assists in maintaining the integrity and security of role configurations across connected systems.

**Technical Impact when configured:**

When this parameter is configured to True, tests executed through the `ConnectorConfigurationTest.aspx` page will assess role content as part of their scope. This provides deeper insights and helps in identifying configuration or role definition issues that might otherwise go unnoticed.

**Examples Scenario:**

An organization wants to ensure that the roles defined within a new HR system do not inadvertently grant excessive permissions. By enabling this parameter, the connector’s test suite will include role content in its evaluation, helping to highlight any potential risks or misconfigurations before the system is fully integrated into the organizational workflow.

**Related Settings:** Not specifically referenced in the provided code snippets.

**Best Practices:** 

- **configure when:** Comprehensive testing is required to ensure that role contents do not contain misconfigurations or excessive permissions that could lead to security risks.
  
- **avoid when:** Testing environments where performance or time constraints are a priority, and a high-level test suffices, you may opt to disable this to streamline the testing process.