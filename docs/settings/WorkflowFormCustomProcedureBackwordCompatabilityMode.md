**Workflow Form Custom Procedure Backward Compatibility Mode**

**Technical Name:** WorkflowFormCustomProcedureBackwordCompatabilityMode

**Category:** Configuration

**Default Value:** Not provided

**Impact Level:** Medium

**Description:** This parameter controls the backward compatibility mode for custom procedures within workflow forms. It is designed for organizations migrating or integrating older custom logic or procedures into the Pathlock Cloud GRC platform's workflow management system.

**Business Impact:** Enabling this mode ensures that legacy custom procedures continue to operate correctly without modification in the new environment. This compatibility is crucial for organizations looking to maintain continuity of workflow processes after system upgrades or during the transition to Pathlock Cloud GRC, mitigating the risk of business process disruptions.

**Technical Impact when configured:** When enabled, this mode may allow for the execution of custom procedures that were designed under older specifications or standards. It affects how the system interprets and runs custom code or scripts linked to workflow forms, potentially affecting performance and security if not managed correctly.

**Examples Scenario:** An organization migrating to Pathlock Cloud GRC from an older system where custom procedures were used extensively for approval workflows. By enabling the Workflow Form Custom Procedure Backward Compatibility Mode, these procedures can still be executed within the new system, ensuring that critical business workflows remain uninterrupted during the transition.

**Related Settings:** 

- `UseSapProfilesAsRoles`
- `UseUserApplicationAreaBeforeObjectApplicationArea`
- `ActiveDirectorySecondaryProviderUsername`
- `ActiveDirectorySecondaryProviderPasswordKey`

**Best Practices:** 

- **Configure when**: Migrating or integrating workflows from systems with significant custom procedural logic to ensure uninterrupted workflow operations.
  
- **Avoid when**: Designing new workflows within the Pathlock Cloud GRC platform. In such cases, it's recommended to use the latest standards and practices for custom procedure implementation to ensure optimal performance and security.