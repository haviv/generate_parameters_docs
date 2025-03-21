# Role Re-Design Mode

**Technical Name:** RoleReDesginMode

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The Role Re-Design Mode parameter is intended for controlling the behavior and functionalities available in the Role Builder Page within the Pathlock Cloud GRC platform. It enables organizations to configure how roles are designed, modified, and visualized, providing a customizable approach to role management in accordance with security and compliance requirements.

**Business Impact:**

Setting this parameter optimally ensures that role management processes align with organizational policies and regulatory compliance standards, mitigating risks associated with inappropriate role access or configurations. It directly influences the efficiency and effectiveness of role engineering tasks, impacting the overall security posture and compliance status of an organization.

**Technical Impact when configured:**

When the Role Re-Design Mode is configured, it directly affects the capabilities available in the Role Builder tool. This includes controlled access to role modification features, adjustment of role visualization settings, and potentially the enforcement of certain compliance or policy constraints during the role design process.

**Examples Scenario:**

For instance, an organization could configure the Role Re-Design Mode to restrict certain role modifications that are not compliant with segregation of duties (SoD) policies, automatically alerting administrators or reverting changes that violate these rules.

**Related Settings:** SoDSimulateForHighRiskRoles

**Best Practices:** 

- **Configure when:** You are establishing or updating role management processes, need to enforce specific security or compliance policies during the role design process, or when there is a need to streamline role management tasks.
  
- **Avoid when:** If the settings could excessively restrict role management capabilities to the point of hindering legitimate operational flexibility or if the organization lacks clear role management policies, as this could lead to unnecessary complexity or misconfigurations.