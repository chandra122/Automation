import os
from dotenv import load_dotenv
import json
from datetime import datetime, timedelta
import schedule
import time
import random
from typing import Dict, List, Optional
from sample_leads import get_sample_leads, get_lead_by_id, get_leads_by_status, get_leads_by_industry

class CRMAutomationBot:
    def __init__(self):
        """
        Initialize the CRM Automation Bot
        """
        self.leads = get_sample_leads()
        self.tasks = []
        self.last_run = {
            'analysis': None,
            'scoring': None,
            'task_check': None
        }
        
    def get_contacts(self, filters: Optional[Dict] = None) -> List[Dict]:
        """
        Retrieve contacts from CRM
        
        Args:
            filters (Dict, optional): Filter criteria for contacts
            
        Returns:
            List[Dict]: List of contact records
        """
        if filters:
            if 'status' in filters:
                return get_leads_by_status(filters['status'])
            if 'industry' in filters:
                return get_leads_by_industry(filters['industry'])
        return self.leads
    
    def update_contact(self, contact_id: str, data: Dict) -> bool:
        """
        Update a contact in CRM
        
        Args:
            contact_id (str): ID of the contact to update
            data (Dict): New contact data
            
        Returns:
            bool: Success status
        """
        print(f"Updating contact {contact_id} with data: {data}")
        return True
    
    def create_task(self, title: str, description: str, due_date: str, assigned_to: str) -> Dict:
        """
        Create a new task in CRM
        
        Args:
            title (str): Task title
            description (str): Task description
            due_date (str): Due date in ISO format
            assigned_to (str): User ID to assign the task to
            
        Returns:
            Dict: Created task data
        """
        task_data = {
            'id': f"TASK{int(time.time())}",
            'title': title,
            'description': description,
            'due_date': due_date,
            'assigned_to': assigned_to,
            'status': 'Pending',
            'created_at': datetime.now().isoformat()
        }
        self.tasks.append(task_data)
        print(f"Created task: {task_data}")
        return task_data
    
    def analyze_contact_interactions(self, contact_id: str) -> Dict:
        """
        Analyze contact interactions using AI
        
        Args:
            contact_id (str): ID of the contact to analyze
            
        Returns:
            Dict: Analysis results
        """
        lead = get_lead_by_id(contact_id)
        if not lead:
            return {
                'error': 'Lead not found',
                'contact_id': contact_id
            }
            
        # Enhanced analysis based on lead data
        priority = 'High' if lead['status'] == 'Qualified' else 'Medium'
        next_action = 'Schedule demo' if lead['status'] == 'New' else 'Follow up call'
        
        # Calculate engagement score
        days_since_contact = (datetime.now() - datetime.strptime(lead['last_contact'], '%Y-%m-%d')).days
        engagement_score = max(0, 100 - (days_since_contact * 5))
        
        # Generate recommendations
        recommendations = []
        if lead['status'] == 'New':
            recommendations.append('Send welcome email')
            recommendations.append('Schedule initial call')
        elif lead['status'] == 'Qualified':
            recommendations.append('Prepare proposal')
            recommendations.append('Schedule demo')
        else:
            recommendations.append('Follow up call')
            recommendations.append('Send relevant case studies')
        
        return {
            'contact_id': contact_id,
            'name': f"{lead['first_name']} {lead['last_name']}",
            'company': lead['company'],
            'priority': priority,
            'next_action': next_action,
            'last_contact': lead['last_contact'],
            'days_since_contact': days_since_contact,
            'engagement_score': engagement_score,
            'recommendations': recommendations,
            'notes': lead['notes']
        }
    
    def generate_lead_score(self, contact_id: str) -> Dict:
        """
        Generate a lead score based on various factors
        
        Args:
            contact_id (str): ID of the contact to score
            
        Returns:
            Dict: Lead scoring results
        """
        lead = get_lead_by_id(contact_id)
        if not lead:
            return {'error': 'Lead not found'}
            
        # Base score components
        status_score = {'New': 20, 'Qualified': 40, 'In Progress': 30}[lead['status']]
        industry_score = {'Technology': 30, 'Healthcare': 25, 'Finance': 25, 'Education': 20, 'Marketing': 20}[lead['industry']]
        title_score = {'CTO': 30, 'Director': 25, 'Manager': 20}[lead['title']]
        
        # Calculate total score
        total_score = status_score + industry_score + title_score
        
        return {
            'contact_id': contact_id,
            'name': f"{lead['first_name']} {lead['last_name']}",
            'company': lead['company'],
            'total_score': total_score,
            'score_components': {
                'status_score': status_score,
                'industry_score': industry_score,
                'title_score': title_score
            }
        }
    
    def check_overdue_tasks(self) -> List[Dict]:
        """
        Check for overdue tasks
        
        Returns:
            List[Dict]: List of overdue tasks
        """
        today = datetime.now().date()
        overdue_tasks = []
        
        for task in self.tasks:
            due_date = datetime.strptime(task['due_date'], '%Y-%m-%d').date()
            if due_date < today and task['status'] == 'Pending':
                overdue_tasks.append(task)
        
        return overdue_tasks
    
    def run_scheduled_tasks(self):
        """Run all scheduled automation tasks"""
        print("\nStarting scheduled tasks...")
        print("Press Ctrl+C to stop the bot")
        
        # Print initial schedule
        print("\nCurrent Schedule:")
        for job in schedule.get_jobs():
            print(f"- {job}")
        
        while True:
            schedule.run_pending()
            time.sleep(1)  # Check every second for pending tasks

def demo_bot_functionality(bot):
    """Demonstrate bot functionality"""
    print("\n=== CRM Automation Bot Demo ===")
    
    # 1. Get all leads
    print("\n1. All Leads:")
    leads = bot.get_contacts()
    for lead in leads:
        print(f"- {lead['first_name']} {lead['last_name']} ({lead['company']})")
    
    # 2. Get qualified leads
    print("\n2. Qualified Leads:")
    qualified_leads = bot.get_contacts({'status': 'Qualified'})
    for lead in qualified_leads:
        print(f"- {lead['first_name']} {lead['last_name']} ({lead['company']})")
    
    # 3. Analyze a lead
    print("\n3. Lead Analysis:")
    analysis = bot.analyze_contact_interactions('LD001')
    print(json.dumps(analysis, indent=2))
    
    # 4. Create a task
    print("\n4. Creating Task:")
    task = bot.create_task(
        title="Follow up call",
        description="Discuss enterprise solutions",
        due_date="2024-03-25",
        assigned_to="sales_rep_1"
    )
    print(json.dumps(task, indent=2))

def scheduled_analysis(bot):
    """Run scheduled analysis on all contacts"""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n{'='*50}")
    print(f"=== Running Scheduled Analysis at {current_time} ===")
    print(f"{'='*50}\n")
    
    # Analyze all contacts
    for contact in bot.get_contacts():
        analysis = bot.analyze_contact_interactions(contact['id'])
        print(f"\nAnalysis for {contact['first_name']} {contact['last_name']}:")
        print(json.dumps(analysis, indent=2))
    
    print(f"\n{'='*50}")
    print("=== Analysis Complete ===")
    print(f"{'='*50}\n")
    bot.last_run['analysis'] = current_time

def scheduled_lead_scoring(bot):
    """Run scheduled lead scoring"""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n{'='*50}")
    print(f"=== Running Lead Scoring at {current_time} ===")
    print(f"{'='*50}\n")
    
    # Score all leads
    for contact in bot.get_contacts():
        score = bot.generate_lead_score(contact['id'])
        print(f"\nLead Score for {contact['first_name']} {contact['last_name']}:")
        print(json.dumps(score, indent=2))
    
    print(f"\n{'='*50}")
    print("=== Lead Scoring Complete ===")
    print(f"{'='*50}\n")
    bot.last_run['scoring'] = current_time

def scheduled_task_check(bot):
    """Check for overdue tasks"""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n{'='*50}")
    print(f"=== Checking Overdue Tasks at {current_time} ===")
    print(f"{'='*50}\n")
    
    overdue_tasks = bot.check_overdue_tasks()
    if overdue_tasks:
        print("\nOverdue Tasks:")
        for task in overdue_tasks:
            print(json.dumps(task, indent=2))
    else:
        print("\nNo overdue tasks found.")
    
    print(f"\n{'='*50}")
    print("=== Task Check Complete ===")
    print(f"{'='*50}\n")
    bot.last_run['task_check'] = current_time

if __name__ == "__main__":
    # Initialize bot
    bot = CRMAutomationBot()
    
    # Run demo
    demo_bot_functionality(bot)
    
    # Schedule different types of tasks
    print("\nScheduling automated tasks...")
    
    # Run analysis every 1 minute
    schedule.every(1).minutes.do(lambda: scheduled_analysis(bot))
    
    # Run lead scoring every 15 minutes
    schedule.every(15).minutes.do(lambda: scheduled_lead_scoring(bot))
    
    # Check for overdue tasks every 10 minutes
    schedule.every(10).minutes.do(lambda: scheduled_task_check(bot))
    
    # Start the scheduler
    bot.run_scheduled_tasks() 