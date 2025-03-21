# Is Demo

**Technical Name:** IsDemo

**Category:** Configuration

**Default Value:** 

**Impact Level:** Low

**Description:** The IsDemo parameter is designed to configure and identify if the current operation or environment is under a demonstration mode. This can impact various functionalities by altering behaviors to suit demo purposes, such as showcasing features without affecting actual data or configurations.

**Business Impact:** Utilizing the IsDemo parameter allows organizations to safely demonstrate the capabilities of the Pathlock Cloud GRC platform without altering or risking the integrity of live data. This is especially useful during presentations, training sessions, or evaluation phases where an authentic experience of the platform is required without actual consequences on the operational environment.

**Technical Impact when configured:** When the IsDemo parameter is configured, certain operations or data manipulations may be restricted or simulated to prevent unintentional changes to live data. This ensures that any operation performed in demo mode serves its illustrative purpose without permanent effects.

**Examples Scenario:** During a sales demonstration for potential clients, the sales team can enable the IsDemo parameter to showcase the platform's functionalities. This allows them to demonstrate user management, risk analysis, and compliance reporting features without compromising security or data integrity of their actual environment.

**Related Settings:** 

- `CommonSettings.Default.IsValidateInstallation` (indirectly related as it pertains to initial setup validations which might be bypassed or altered in demo modes in certain contexts).

**Best Practices:** configure when engaging in demonstrations, training, or presentations where it's crucial to exhibit platform capabilities without altering real data. Avoid when performing actual data management and operation tasks that require changes to be saved and reflected in the system.