# Enable Impact Analysis Calculator

**Technical Name:** EnableImpactAnalysisCalculator

**Category:** Workflow

**Default Value:** 

**Impact Level:** High

**Description:**

This setting enables the Impact Analysis Calculator within the Pathlock Cloud GRC platform, supporting the assessment and evaluation of potential changes or actions' impacts on security, risk, and compliance postures.

**Business Impact:**

Activating this feature allows organizations to proactively gauge the effects of proposed changes within their systems, particularly assessing risks, compliance breaches, or security vulnerabilities before they are implemented. This foresighted analysis aids in preventing costly errors, ensuring compliance standards are met, and maintaining robust security postures.

**Technical Impact when configured:**

Upon configuration, the Impact Analysis Calculator will analyze the outcomes of simulations performed on user actions or system changes. It utilizes detailed simulation results and user activities to calculate potential impacts, enabling informed decision-making regarding system modifications or policy updates.

**Examples Scenario:**

A company planning to modify its access control policies can use the Impact Analysis Calculator to simulate the proposed changes' impact on user roles and permissions. By analyzing the simulation results, the company can identify if the proposed changes would inadvertently grant excessive privileges to certain roles, potentially violating compliance standards or exposing the system to security risks.

**Related Settings:**

- CommentForApplyChangesThroughAuthorizationSimulation

**Best Practices:** configure when initiating any change that could impact your security, compliance, or risk posture. Avoid usage during trivial changes that do not affect these areas.