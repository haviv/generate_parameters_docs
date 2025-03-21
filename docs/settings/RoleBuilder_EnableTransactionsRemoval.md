# Role Builder Enable Transactions Removal

**Technical Name:** RoleBuilder_EnableTransactionsRemoval

**Category:** Configuration

**Default Value:** False

**Impact Level:** Medium

**Description:**

Enables users to remove transactions and authorization objects from roles within the Pathlock Cloud GRC platform's Role Builder feature.

**Business Impact:**

Implementing this parameter allows administrators to refine roles by removing unnecessary or risky transactions and authorization objects directly from the Role Builder interface, enhancing security and compliance by ensuring roles are tightly scoped to user needs.

**Technical Impact when configured:**

When enabled, the Role Builder page will allow the removal of specified transactions and authorization objects for a given role. This directly affects the authorization model by potentially altering users' access rights, which might lead to changes in how users interact with the target systems.

**Examples Scenario:**

- **Before Configuration:** An organization notices that multiple roles contain transactions that are no longer necessary or present a segregation of duties (SoD) risk.
  
- **After Configuration:** The administrator enables `RoleBuilder_EnableTransactionsRemoval` and uses the Role Builder to remove these risky transactions. As a result, roles are streamlined, and compliance with internal and external audit requirements is improved.

**Related Settings:** SodCheckForSingleSystemOnly

**Best Practices:** 

- **Configure when:** Refining roles for security and compliance purposes or when unnecessary transactions are discovered within roles.
- **Avoid when:** Transactions and authorization objects in roles must remain static for auditing or historical reasons.