# Enable Delete Action

**Technical Name:** EnableDeleteAction

**Category:** Workflow

**Default Value:** Not Provided

**Impact Level:** High

**Description:** Allows administrators to enable or disable the ability to delete actions within the platform's workflow management UI. This parameter ensures that workflow actions, including critical operations, are controlled and potentially hazardous operations are managed securely.

**Business Impact:** Enabling the delete action can streamline operational workflows by allowing unnecessary or outdated actions to be removed, thereby reducing clutter and potential confusion. Conversely, disabling it can prevent accidental or malicious deletions, ensuring the integrity and stability of workflow operations critical to governance, risk, and compliance strategies.

**Technical Impact when configured:** Configuring this option affects how users can interact with workflow actions within the UI. When enabled, users with the necessary permissions can delete actions. When disabled, all delete action functionalities are removed from the UI, preventing any alterations that could compromise workflow processes.

**Examples Scenario:** An organization may enable this feature during a system cleanup or restructuring phase to allow administrators to remove obsolete actions. Alternatively, during operational periods where stability is paramount, the feature may be disabled to protect against accidental deletions of critical workflow actions.

**Related Settings:** 

- `EnableApprovedEmergencyAccess`
- `EnableAutosaveOptions`

**Best Practices:** 

- **Configure when:** System maintenance or cleanup is required, and there is a need to remove obsolete or redundant actions. Only users who understand the implications of deleting actions should be given access.
  
- **Avoid when:** The system is in a stable operational state, and all defined actions are necessary for daily operations. To prevent accidental or unauthorized changes, keep this feature disabled.