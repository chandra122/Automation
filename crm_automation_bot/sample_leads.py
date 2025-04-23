SAMPLE_LEADS = [
    {
        "id": "LD001",
        "first_name": "John",
        "last_name": "Smith",
        "company": "Tech Solutions Inc.",
        "email": "john.smith@techsolutions.com",
        "phone": "+1 (555) 123-4567",
        "title": "CTO",
        "industry": "Technology",
        "status": "New",
        "source": "Website",
        "created_date": "2024-03-15",
        "last_contact": "2024-03-20",
        "notes": "Interested in enterprise solutions. Requested demo."
    },
    {
        "id": "LD002",
        "first_name": "Sarah",
        "last_name": "Johnson",
        "company": "Global Marketing Group",
        "email": "sarah.j@globalmarketing.com",
        "phone": "+1 (555) 234-5678",
        "title": "Marketing Director",
        "industry": "Marketing",
        "status": "Qualified",
        "source": "Referral",
        "created_date": "2024-03-10",
        "last_contact": "2024-03-18",
        "notes": "Looking for CRM integration with marketing tools."
    },
    {
        "id": "LD003",
        "first_name": "Michael",
        "last_name": "Brown",
        "company": "Healthcare Systems",
        "email": "m.brown@healthcaresys.com",
        "phone": "+1 (555) 345-6789",
        "title": "IT Manager",
        "industry": "Healthcare",
        "status": "In Progress",
        "source": "Trade Show",
        "created_date": "2024-03-05",
        "last_contact": "2024-03-19",
        "notes": "Needs HIPAA compliance features. Budget approved."
    },
    {
        "id": "LD004",
        "first_name": "Emily",
        "last_name": "Davis",
        "company": "EduTech Solutions",
        "email": "emily.d@edutech.com",
        "phone": "+1 (555) 456-7890",
        "title": "Operations Manager",
        "industry": "Education",
        "status": "New",
        "source": "Social Media",
        "created_date": "2024-03-22",
        "last_contact": "2024-03-22",
        "notes": "Interested in student management features."
    },
    {
        "id": "LD005",
        "first_name": "David",
        "last_name": "Wilson",
        "company": "Financial Services Corp",
        "email": "d.wilson@financialcorp.com",
        "phone": "+1 (555) 567-8901",
        "title": "Finance Director",
        "industry": "Finance",
        "status": "Qualified",
        "source": "Email Campaign",
        "created_date": "2024-03-12",
        "last_contact": "2024-03-17",
        "notes": "Looking for financial reporting features. High priority."
    }
]

def get_sample_leads():
    """
    Returns the list of sample leads for testing purposes.
    """
    return SAMPLE_LEADS

def get_lead_by_id(lead_id):
    """
    Returns a specific lead by ID.
    
    Args:
        lead_id (str): The ID of the lead to retrieve
        
    Returns:
        dict: The lead data if found, None otherwise
    """
    for lead in SAMPLE_LEADS:
        if lead["id"] == lead_id:
            return lead
    return None

def get_leads_by_status(status):
    """
    Returns all leads with a specific status.
    
    Args:
        status (str): The status to filter by
        
    Returns:
        list: List of leads matching the status
    """
    return [lead for lead in SAMPLE_LEADS if lead["status"] == status]

def get_leads_by_industry(industry):
    """
    Returns all leads in a specific industry.
    
    Args:
        industry (str): The industry to filter by
        
    Returns:
        list: List of leads in the specified industry
    """
    return [lead for lead in SAMPLE_LEADS if lead["industry"] == industry] 