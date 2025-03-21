# Custom Central User Administration System Number

**Technical Name:** CustomCUASystemNumber

**Category:** Configuration

**Default Value:** None

**Impact Level:** High

**Description:**

The Custom Central User Administration (CUA) System Number parameter is utilized for defining a unique system identifier within the Pathlock Cloud GRC platform for connections that employ Central User Administration. This system number is critical in environments where CUA is enabled, as it distinguishes the specific CUA system from other systems connected to the platform.

**Business Impact:**

Configuring the CustomCUASystemNumber correctly ensures that user administration actions (such as role assignments and user information updates) are accurately propagated through the CUA system. It prevents potential conflicts or misconfigurations that could result in access issues or compliance violations across interconnected systems.

**Technical Impact when configured:**

- Ensures smooth and error-free communication between the Pathlock platform and the SAP CUA system.
- Helps in maintaining consistent user identity and access management across multiple systems.
- Facilitates accurate role assignments and access rights validations.

**Examples Scenario:**

An organization uses Pathlock for GRC in a landscape with multiple SAP systems. They employ CUA to manage users centrally. The organization needs to configure the CustomCUASystemNumber to specify which SAP system, identified by the system number, serves as the CUA. This ensures that all user management activities conducted from Pathlock are correctly targeted and executed in the CUA system, maintaining integrity and compliance across the enterprise.

**Related Settings:**

- EnableCUA
- DisableCua

**Best Practices:** 

- Configure when setting up Pathlock in an environment where SAP CUA is used to manage user roles and permissions centrally.
- Avoid configuration errors by confirming the system number with the SAP BASIS team to ensure accurate system identification.