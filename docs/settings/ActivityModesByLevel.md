# Activity Modes By Level

**Technical Name:** ActivityModesByLevel

**Category:** Reporting

**Default Value:** Not specified

**Impact Level:** Medium

**Description:**

The parameter 'Activity Modes By Level' is designed to facilitate enhanced reporting within the Pathlock Cloud GRC platform, particularly in scenarios involving user activity across various systems, such as Active Directory. It enables the inclusion or exclusion of specific activity modes (e.g., create, modify, delete) in reports at different hierarchical levels.

**Business Impact:**

Employing this parameter allows for more granular control and visibility over user activities, aiding in auditing and compliance efforts. Organizations can more easily identify and address potentially unauthorized or risky changes, thereby enhancing their security posture and compliance with regulatory requirements.

**Technical Impact when configured:**

When this parameter is configured, it impacts how activity data is retrieved and presented in reports. Specifically, it allows for the filtering of activities based on their modes at different levels of detail, ensuring that reports can be tailored to focus on the most relevant information for audit or compliance checks.

**Examples Scenario:**

- **Audit Preparation:** When preparing for an audit, an organization can configure this parameter to include only 'delete' activities across specific systems, streamlining the process of auditing deletions for unauthorized or accidental data removal.
  
- **Compliance Monitoring:** In a scenario where compliance with data protection regulations requires monitoring of data creation or modification, this parameter can be set to include only these activity modes, aiding in the detection and investigation of non-compliant actions.

**Related Settings:**

N/A

**Applicable Workflows Actions:** 

N/A

**Best Practices:** 

- **Configure when:** Preparing for audits or compliance checks that require focused reports on specific types of user activities.
  
- **Avoid when:** Broad overview reports of user activities are needed, where filtering out specific activity modes may omit relevant information.