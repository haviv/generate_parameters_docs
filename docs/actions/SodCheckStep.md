# SodCheckStep

**Action Name:** SodCheckStep

**Category:** SOD (Segregation of Duties)

**Description:** The SodCheckStep is a specialized workflow step designed to perform comprehensive Segregation of Duties (SoD) validation during access request workflows within the Pathlock Cloud platform. This step automatically analyzes the requested roles and transactions against existing user permissions to identify potential SoD violations that could create conflicts of interest or security risks. When violations are detected, the step generates a detailed HTML table containing violation information and either requires manual approval or automatically continues based on configuration. The step supports multiple instance modes, allowing separate SoD checks for different systems, schemas, and company codes, ensuring granular control over the approval process.

**Parameters:**

**Basic:**
- **AllowMultipleInstancesForSystems** (Boolean): Enables creation of separate SoD check instances for each system involved in the request
- **AllowMultipleInstancesForSchemas** (Boolean): Enables creation of separate SoD check instances for each schema involved in the request  
- **AllowMultipleInstancesForCompanyCodes** (Boolean): Enables creation of separate SoD check instances for each company code involved in the request
- **MinimumRiskLevelForSoDCheck** (String): Sets the minimum risk severity level that will trigger SoD violations (selectable from configured severity levels)

**Advanced:**
- **SodCheckAndContinue** (Boolean): When enabled, allows the workflow to continue automatically even when SoD violations are found, bypassing manual approval
- **ShowSodAsImpactAnalysis** (Boolean): Controls whether SoD violations are displayed as impact analysis risks in addition to standard violation reporting
- **SodCheckStep_GenerateSodTableWithDescription** (Boolean): Includes detailed descriptions in the SoD violation table when available

**Business Impact:** The SodCheckStep is fundamental to maintaining organizational governance, risk management, and compliance (GRC) by preventing unauthorized access combinations that could lead to fraud, errors, or policy violations. By automatically identifying when users would gain conflicting access rights, organizations can enforce proper segregation controls, reduce audit findings, and maintain regulatory compliance. The step's flexible configuration allows organizations to balance security requirements with operational efficiency, supporting both strict approval workflows and automated processing where appropriate.

**Example of Usage:** When a user requests access to both accounts payable creation and approval roles, the SodCheckStep would detect this as a potential SoD violation since the same person could create and approve their own transactions. The step would generate a detailed report showing the conflicting roles and require approval from designated authorities before proceeding with the access grant.

**Prerequisites:** Before executing the SodCheckStep:
- A valid WorkflowInstance must contain either role requests (WorkflowAffectedRoles) or transaction requests (WorkflowAuthorizationRequests)
- SoD combination rules must be properly configured in the system through WorkflowApprovalGroupType and CombinationSchema settings
- The executing user must have sufficient permissions to access SoD analysis services and user role information
- ProfileTailorContext must be properly initialized for the target system(s)

**Error Handling and Troubleshooting:**

**Common Error:** "User Has Full Authorization" message appears in step comments
- **Probable Cause:** Exception occurred during SoD calculation, typically due to role data access issues or service configuration problems
- **Solution:** Verify user permissions, check ProfileTailorContext initialization, and review SodSoxServices configuration

**Common Error:** Step is automatically skipped without processing
- **Probable Cause:** No roles or transactions found in the workflow request, or request data is incomplete
- **Solution:** Ensure WorkflowAuthorizationRequests contains valid role or transaction data before reaching the SoD check step

**Common Error:** Multiple instances not created despite configuration
- **Probable Cause:** SoD results don't contain the expected system/schema/company code variations, or parameters are not properly configured
- **Solution:** Verify the AllowMultipleInstances parameters are set correctly and that the request actually spans multiple systems/schemas/company codes

**Common Error:** Empty or malformed SoD violation table
- **Probable Cause:** SodSoxServices configuration issues or missing combination rules
- **Solution:** Verify SoD combination schemas are properly configured in WorkflowApprovalGroupType and that the SodSoxServices can access the required data sources

**Generated Fields for Email Templates:**
- **Comments:** Contains the complete HTML-formatted SoD violation table with headers, violation details, and affected roles
- **AlternativeAffectedRoles:** Comma-separated list of roles involved in SoD violations
- **SodResultsForSystem:** System name for the current SoD check instance
- **SodResultsForSchema:** Schema name for the current SoD check instance  
- **SodResultsForCompanyCode:** Company code for the current SoD check instance