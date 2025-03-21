# Combination Object

**Technical Name:** CombinationObject

**Category:** Compliance

**Default Value:** Not Applicable

**Impact Level:** High

**Description:**

The Combination Object parameter plays a crucial role in configuring and managing Segregation of Duties (SoD) policies and monitoring Simultaneous Usage within the Pathlock Cloud GRC platform. It is instrumental in ensuring that user access rights are compliant with internal and external regulations, thereby minimizing risk.

**Business Impact:**

Implementing strict SoD policies and controlling simultaneous access are critical for preventing fraud and ensuring that critical tasks are segregated among multiple users. Misconfiguration of this parameter can lead to a lack of compliance, increased risk of internal fraud, and potential breaches of external regulations.

**Technical Impact when configured:**

Proper configuration of the Combination Object parameter enhances the monitoring capabilities of the platform, ensuring that organizations can effectively enforce SoD policies and prevent unauthorized simultaneous access to sensitive systems or data.

**Examples Scenario:**

An organization uses the Combination Object parameter to define SoD policies that prevent the same user from creating and approving purchase orders, significantly reducing the risk of fraudulent activity within procurement processes.

**Related Settings:** 

- CommonSettings.Default.RolesRegistryNodes
- CommonSettings.Default.GlobalAdministrator

**Best Practices:** 

- **Configure when:** Establishing or updating SoD policies and access controls. Use to accurately define roles and responsibilities, ensuring they align with compliance requirements.
  
- **Avoid when:** Insufficient information is available to define clear SoD policies and access controls to prevent disruptions in workflow or unnecessary access restrictions.