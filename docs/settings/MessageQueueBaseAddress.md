# Message Queue Base Address

**Technical Name:** MessageQueueBaseAddress

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:** The Message Queue Base Address parameter specifies the foundational network address used for message queuing services. This setting is crucial for enabling communication between different components of the Pathlock GRC platform, particularly for asynchronous data processing and integration activities.

**Business Impact:** Proper configuration of the Message Queue Base Address is vital for maintaining the efficiency and reliability of the Pathlock GRC platform's communication infrastructure. It ensures that tasks related to security, risk, and compliance management are executed promptly, supporting the organization's overall governance framework.

**Technical Impact when configured:** When configured correctly, the Message Queue Base Address facilitates seamless data exchange across distributed services, enhancing the system’s scalability and fault tolerance. Misconfiguration may lead to communication failures, delayed processing, or system downtime, affecting operational efficiency and decision-making processes.

**Examples Scenario:** An organization implements a new policy requiring real-time audit log processing. By configuring the Message Queue Base Address, the Pathlock GRC platform can efficiently route audit logs to the appropriate processing service, ensuring timely compliance checks and reporting.

**Related Settings:** 

**Best Practices:** configure when establishing initial system setup or when modifying the network infrastructure to ensure continuous and reliable message queuing. Avoid when the network setup is under review or incomplete to prevent misconfigurations.