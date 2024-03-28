# Call Center: Imagine you have a call center with three levels of employees: respondent, manager, and director.
# An incoming telephone call must first be allocated to a respondent who is free. If the respondent can't handle the
# call, he or she must escalate the call to a manager. If the manager is not free or not able to handle it, then the
# call should be escalated to a director. Design the classes and data structures for this problem. Implement a method
# dispatchCall() which assigns a call to the first available employee.
#
# A Call class with an a call_Id and an assigned_to list with ID of each respondent who got assigned to them.
# Calls go into respondent_queue (first in first out). There are be 3 "call waiting" queues: respondents,
# managers, and directors would all have their own call waiting qs. "call takers" would have their own queues with their
# employee IDs in them. Calls would deque by checking the associated call-taker q. If no call takers were available,
# the calls would just continue to queue up. The respondents would be able to call a method that moves the call to the
# manager queue, and managers could call a method that moves the call to the director queue or the respondent queue.
# in the case of a higher level employee sending a call back down to a lower level employee (like a manager sending the
# call back to a respondent) I would have "call waiting" stacks that would have priority over the queues. This could
# be done with a priority queue instead, but I am anticipating this scenario to be uncommon and may want to keep the
# main call waiting queue as simple as possible.


from collections import deque

def main():
    class Call:
        def __init__(self, call_id: int):
            self.call_id = call_id
            self.assigned_to = None

    class Employee:
        def __init__(self, title: str, employee_id: int, name: str):
            self.title = title
            self.employee_id = employee_id
            self.name = name
            self.available = True

        def set_availability(self, new_availability_status: bool):
            self.available = new_availability_status

    def dispatch_call(call: Call, q_list: list, call_q: deque):
        for q in q_list:
            if not call.assigned_to:
                for employee in q:
                    if employee.available:
                        call.assigned_to = employee.employee_id
                        employee.available = False
                        q.popleft()
                        break
            else:
                break
        if call.assigned_to:
            print(f"Call id {call.call_id} is assigned to employee ID {call.assigned_to}.")
        else:
            print(f"All operators are busy. Call ID {call.call_id} will have to hold.")
            call_q.append(call)

    def initialize_employees():
        response = {}
        respondents_name_list = ["Bob", "Alice", "Jim", "Denise"]
        managers_name_list = ["Dorothy", "Simon"]
        directors_name_list = ["Gerald"]
        employee_id = 1
        for name in respondents_name_list:
            title = "respondent"
            employee_id_prefix = 1
            employee_id_with_prefix = int(f"{employee_id_prefix}{employee_id}")
            response[f"employee_id_{employee_id_with_prefix}"] = Employee(title, employee_id_with_prefix, name)
            employee_id += 1
        for name in managers_name_list:
            title = "manager"
            employee_id_prefix = 3
            employee_id_with_prefix = int(f"{employee_id_prefix}{employee_id}")
            response[f"employee_id_{employee_id_with_prefix}"] = Employee(title, employee_id_with_prefix, name)
            employee_id += 1
        for name in directors_name_list:
            title = "director"
            employee_id_prefix = 7
            employee_id_with_prefix = int(f"{employee_id_prefix}{employee_id}")
            response[f"employee_id_{employee_id_with_prefix}"] = Employee(title, employee_id_with_prefix, name)
            employee_id += 1
        return response

    def initialize_queue(employees_dict: dict, title: str):
        q = deque()
        for employee in employees_dict:
            if employees_dict[employee].title.lower() == title.lower() and employees_dict[employee].available:
                q.append(employees_dict[employee])
        return q

    employees_dict = initialize_employees()
    respondents_q = initialize_queue(employees_dict, "respondent")
    managers_q = initialize_queue(employees_dict, "manager")
    directors_q = initialize_queue(employees_dict, "director")
    q_list = [respondents_q, managers_q, directors_q]
    call_q = deque()
    call_dict = {}
    for call_id in range(0, 20):
        call_dict[call_id] = Call(call_id)
    for call in call_dict:
        dispatch_call(call_dict[call], q_list, call_q)

main()
