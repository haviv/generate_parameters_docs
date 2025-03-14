# `SystemWideSystemId` Parameter Documentation

## Category
Configuration/Setup

## Default Value
Not explicitly mentioned in the provided code snippets. The default value is typically defined in the application's settings or configuration files.

## Impact Level
High

## Description
The `SystemWideSystemId` parameter is used within the Pathlock Cloud GRC platform to define a system-wide identifier which applies across multiple components of the application. This ID is utilized when a specific system ID is not provided or needs to be overridden by a global setting.

## Business Impact
Setting the correct `SystemWideSystemId` is crucial for maintaining the integrity of risk and compliance data across the organization. It ensures that operations such as role assignment, workflow execution, SoD (Segregation of Duties) calculation for business roles, and profile context initialization reference the correct system entity. Incorrect configuration can lead to mismanaged access controls, inaccurate risk assessments, and non-compliance incidents.

## Technical Impact when configured
- Initializes the application context with a global system ID if a more specific context is not available.
- Ensures workflow actions, and SoD calculations for entities default to a consistent system reference in absence of a specified system ID.
- Facilitates correct data retrieval and process execution across the Pathlock platform, leveraging a consistent system identifier.

## Examples Scenario
In an organization using Pathlock to manage GRC across multiple SAP systems, the `SystemWideSystemId` can be set to refer to the primary SAP system's ID. This ensures that, by default, any operations not explicitly tied to alternative systems still execute against this primary system, maintaining operational continuity and compliance integrity.

**Example:**
An administrator sets the `SystemWideSystemId` to `1000`, designating the primary SAP system. When a new workflow is initiated without a specific system ID, it inherits the ID `1000`, ensuring it operates within the context of the primary system.

## Related Settings
- `IsCloud`: Determines if the settings are applied cloud-wide.
- `EnableSoDCalculationByEntityForBusinessRoles`: Flags whether SoD calculation by entity for business roles is enabled, which also depends on the `SystemWideSystemId`.

## Best Practices
- **Configure when:** 
  - You have a primary system that will serve as the default context for operations within the Pathlock platform.
  - You need to ensure fallback to a consistent system ID for various operations to maintain operational and compliance integrity.
- **Avoid when:**
  - Each operation or process requires a distinct system context, and defaulting to a global ID could cause data integrity or compliance issues.
  - The organization does not have a clear primary system that can serve as a default context for unspecified operations.

## Context
The `SystemWideSystemId` parameter is a fundamental setting within the Pathlock Cloud GRC platform that influences how data is associated, accessed, and processed across the platform, affecting security, compliance, and operational effectiveness. Proper configuration aligns the platform's operation with the organization's structure and compliance requirements, ensuring effective governance, risk management, and compliance (GRC) practices.