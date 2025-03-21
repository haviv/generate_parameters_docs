**Technical Name: MainEntityName**

**Category:** Workflow

**Default Value:** None

**Impact Level:** High

**Description:**

The `MainEntityName` parameter is utilized in the Pathlock Cloud GRC platform to specify the primary entity for smart queries and user-group rule imports. It serves as a key factor in defining the scope and target of various security, compliance, and risk management workflows within the system.

**Business Impact:**

Specifying the correct `MainEntityName` ensures that security and compliance checks are accurately scoped to the relevant data entities, enhancing the effectiveness of governance, risk, and compliance activities. It directly impacts the accuracy of reporting, the effectiveness of security measures, and compliance with regulatory requirements.

**Technical Impact when configured:**

Once configured, `MainEntityName` enables targeted querying and applies specific rules or policies to the designated main entity. It significantly influences the performance and relevance of the system's security, compliance, and risk management functionalities by ensuring that operations are executed in the context of the correct data entity.

**Example Scenario:**

- In a scenario where an organization needs to apply specific compliance rules to user groups, the `MainEntityName` can be set to "UserGroup". This will ensure that any smart queries or rules defined in the system are accurately applied to the user groups within the organization, thereby achieving compliance with internal policies or external regulations.

**Related Settings:**

- SmartQueryManager
- ExpressionSerializer

**Best Practices:**

- **configure when:** You have a clear understanding of the entities within your GRC platform and need to apply specific rules or filters to one of them.
- **avoid when:** The scope of the configuration is not clear, or it could potentially apply broad, unintended changes to the system's behavior.