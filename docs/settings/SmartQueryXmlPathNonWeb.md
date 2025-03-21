# Smart Query Xml Path Non Web

**Technical Name:** SmartQueryXmlPathNonWeb

**Category:** Configuration

**Default Value:**

**Impact Level:** High

**Description:**
The `SmartQueryXmlPathNonWeb` parameter specifies the file system path to the XML directories and files used by the Pathlock Cloud GRC platform for non-web based operations. This parameter is critical for ensuring that XML-based configurations, permissions, and tests within Pathlock are correctly located and accessed, particularly for background services or processes that do not interact with the web interface.

**Business Impact:**
Proper configuration of this parameter ensures that Pathlock Cloud GRC can accurately perform configuration tests, apply permissions, and manage data connections for non-web applications and services. Misconfiguration may lead to system failures, inability to enforce compliance rules, or incorrect risk assessments.

**Technical Impact when configured:**
- Enables the Pathlock system to correctly locate and access XML files for configuration tests, permissions sets, and other non-web based functionalities.
- Ensures that background operations related to security, risk, and compliance management have the necessary data structure support for successful execution.

**Examples Scenario:**
A company needs to ensure that its non-web based background services, which handle sensitive compliance testing and configuration validation, can accurately locate and utilize XML files for operations. By correctly setting the `SmartQueryXmlPathNonWeb` parameter, they ensure these services run smoothly, supporting the organization's compliance and risk management strategies without interruption.

**Related Settings:**
- CommonSettings.Default.ServiceConfigurationTester
- CommonSettings.Default.SendMailOnWorkflowStarted
- CommonSettings.Default.SendMailOnWorkflowApproved
- CommonSettings.Default.SendMailOnWorkflowDeclined

**Best Practices:** 
- Configure when setting up or migrating Pathlock services to a new server environment to ensure that all non-web based operations can accurately locate necessary XML resources.
- Avoid when operations and configurations are strictly web-based or do not require access to a file system path for XML resources.