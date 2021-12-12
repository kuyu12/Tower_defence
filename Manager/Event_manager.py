from pydispatch import dispatcher

from Utils.Enums import Signals, Stage_State, Action


class EventManager:
    def __init__(self):
        dispatcher.connect(self.handle_tower_selected_event, signal=Signals.Tower_Selected, sender=dispatcher.Any)
        dispatcher.connect(self.handle_tower_deselected_event, signal=Signals.Tower_Deselected, sender=dispatcher.Any)
        dispatcher.connect(self.handle_tower_placed_event, signal=Signals.Tower_Placed, sender=dispatcher.Any)
        dispatcher.connect(self.handle_add_enemy_action, signal=Signals.Add_Enemy, sender=dispatcher.Any)
        dispatcher.connect(self.handle_tower_method_change, signal=Signals.Tower_Attack_Method_Change,
                           sender=dispatcher.Any)
        dispatcher.connect(self.handle_tower_attack_enemy, signal=Signals.Tower_Attack_Enemy, sender=dispatcher.Any)
        dispatcher.connect(self.handle_enemy_remove_action, signal=Signals.Remove_Enemy, sender=dispatcher.Any)


        self.current_event = None
        self.last_event = None

        self.stage_state = Stage_State.Normal

        self.on_stage_state_change = None
        self.on_action = None
        self.enemy_action = None

    def set_stage_state(self, Stage):
        self.stage_state = Stage

    def handle_tower_selected_event(self, sender, event):
        self.handle_event(sender, event, Stage_State.Tower_Selected)

    def handle_tower_deselected_event(self, sender, event):
        self.handle_event(sender, event, Stage_State.Normal)

    def handle_tower_placed_event(self, sender, event):
        self.handel_action(self, event, Action.Tower_Placed)

    def handle_add_enemy_action(self, sender, event):
        self.enemy_action(event,Action.Add_Enemy)

    def handle_enemy_remove_action(self, sender, event):
        self.enemy_action(event,Action.Remove_Enemy)

    def handle_tower_method_change(self, sender, event):
        self.handel_action(sender, event, Action.Tower_Attack_Method_Change)

    def handle_tower_attack_enemy(self, sender, event):
        self.handel_action(sender, event, Action.Tower_Attack_Enemy)

    def handle_event(self, sender, event, state):
        print("\nSignal Receive:", event.signal, "\nFrom:", event.sender, "\nData:", event.data, "\nTime:", event.time)
        self.last_event = self.current_event
        self.current_event = event
        self.stage_state = state
        self.stage_state_change(self.stage_state, self.current_event)

    def handel_action(self, sender, event, action):
        print("\nSignal Receive:", event.signal, "\nFrom:", event.sender, "\naction:", action, "\nData:", event.data,
              "\nTime:", event.time)
        self.active_listener(action, event)

    def active_listener(self, action, event):
        if self.on_action:
            self.on_action(action, event)

    def stage_state_change(self, state, event):
        if self.on_stage_state_change:
            self.on_stage_state_change(state, event)
