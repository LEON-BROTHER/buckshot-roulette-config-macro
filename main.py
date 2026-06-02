import pyautogui
import time
import json
import tkinter as tk

EXECUTE_MODE = "execute" 

current_screen_width, current_screen_height = pyautogui.size()

TARGET_RESOLUTION = f"{current_screen_width}x{current_screen_height}"

class Config:
    def __init__(self):
        self.starting_health = -1
        self.items = {}
        self.items["hand saw"] = [2, 32, True]
        self.items["magnifying glass"] = [2, 32, True]
        self.items["jammer"] = [1, 1, True]
        self.items["cigarette pack"] = [1, 32, True]
        self.items["beer"] = [8, 32, True]
        self.items["burner phone"] = [8, 32, True]
        self.items["adrenaline"] = [4, 32, True]
        self.items["inverter"] = [4, 32, True]
        self.items["remote"] = [1, 2, True]
        self.sequences = [
            [-1,-1,-1],
            [-1,-1,-1],
            [-1,-1,-1],
            [-1,-1,-1]
        ]

    def enterConf(self):
        default_config = Config()
        config = self

        if config.starting_health != default_config.starting_health:
            if config.starting_health == -1:
                pyautogui.click(pos.random_starting_health_pos)
                default_config.starting_health = -1
                time.sleep(click_wait)
            else:
                while config.starting_health != default_config.starting_health:
                    if config.starting_health > default_config.starting_health:
                        pyautogui.click(pos.plus_starting_health_pos)
                        default_config.starting_health += 1
                    else:
                        pyautogui.click(pos.minus_starting_health_pos)
                        default_config.starting_health -= 1
                    time.sleep(click_wait)

        for item in config.items:
            if item not in default_config.items:
                continue
            if config.items[item][0] != default_config.items[item][0]:
                for i in range(9):
                    if item == list(config.items.keys())[i]:
                        while config.items[item][0] != default_config.items[item][0]:
                            if config.items[item][0] > default_config.items[item][0]:
                                pyautogui.click(pos.item_player_pos[0], pos.item_player_pos[1]+i*pos.item_y_space)
                                default_config.items[item][0] += 1
                            else:
                                pyautogui.click(pos.item_player_pos[0], pos.item_player_pos[1]+i*pos.item_y_space, button='right')
                                default_config.items[item][0] -= 1
                            time.sleep(click_wait)
            if config.items[item][1] != default_config.items[item][1]:
                for i in range(9):
                    if item == list(config.items.keys())[i]:
                        while config.items[item][1] != default_config.items[item][1]:
                            if config.items[item][1] > default_config.items[item][1]:
                                pyautogui.click(pos.item_table_pos[0], pos.item_table_pos[1]+i*pos.item_y_space)
                                default_config.items[item][1] += 1
                            else:
                                pyautogui.click(pos.item_table_pos[0], pos.item_table_pos[1]+i*pos.item_y_space, button='right')
                                default_config.items[item][1] -= 1
                            time.sleep(click_wait)
            if config.items[item][2] != default_config.items[item][2]:
                for i in range(9):
                    if item == list(config.items.keys())[i]:
                        pyautogui.click(pos.item_enabled_pos[0], pos.item_enabled_pos[1]+i*pos.item_y_space)
                        default_config.items[item][2] = not default_config.items[item][2]
                        time.sleep(click_wait)

        for i in range(4):
            lives_higher = config.sequences[i][1] > config.sequences[i][0]
            cur_row = 0
            cur_pos_random = pos.random_seq_blanks_pos
            cur_pos_plus = pos.plus_seq_blanks_pos
            cur_pos_minus = pos.minus_seq_blanks_pos

            if lives_higher:
                cur_row = 1       
                cur_pos_random = pos.random_seq_lives_pos
                cur_pos_plus = pos.plus_seq_lives_pos
                cur_pos_minus = pos.minus_seq_lives_pos

            if config.sequences[i][cur_row] != default_config.sequences[i][cur_row]:
                if config.sequences[i][cur_row] == -1:
                    pyautogui.click(cur_pos_random[0], cur_pos_random[1]+i*pos.seq_y_space)
                    default_config.sequences[i][cur_row] = -1
                    time.sleep(click_wait)
                else:
                    while config.sequences[i][cur_row] != default_config.sequences[i][cur_row]:
                        if config.sequences[i][cur_row] > default_config.sequences[i][cur_row]:
                            pyautogui.click(cur_pos_plus[0], cur_pos_plus[1]+i*pos.seq_y_space)
                            if default_config.sequences[i][cur_row] == -1:
                                default_config.sequences[i][1] += 1
                                default_config.sequences[i][0] += 1
                            default_config.sequences[i][cur_row] += 1
                        else:
                            pyautogui.click(cur_pos_minus[0], cur_pos_minus[1]+i*pos.seq_y_space)
                            default_config.sequences[i][cur_row] -= 1
                        time.sleep(click_wait)

            if lives_higher:
                cur_row = 0
                cur_pos_random = pos.random_seq_blanks_pos
                cur_pos_plus = pos.plus_seq_blanks_pos
                cur_pos_minus = pos.minus_seq_blanks_pos
            else:
                cur_row = 1
                cur_pos_random = pos.random_seq_lives_pos
                cur_pos_plus = pos.plus_seq_lives_pos
                cur_pos_minus = pos.minus_seq_lives_pos

            if config.sequences[i][cur_row] != default_config.sequences[i][cur_row]:
                if config.sequences[i][cur_row] == -1:
                    pyautogui.click(cur_pos_random[0], cur_pos_random[1]+i*pos.seq_y_space)
                    default_config.sequences[i][cur_row] = -1
                    time.sleep(click_wait)
                else:
                    while config.sequences[i][cur_row] != default_config.sequences[i][cur_row]:
                        if config.sequences[i][cur_row] > default_config.sequences[i][cur_row]:
                            pyautogui.click(cur_pos_plus[0], cur_pos_plus[1]+i*pos.seq_y_space)
                            if default_config.sequences[i][cur_row] == -1:
                                default_config.sequences[i][1] += 1
                                default_config.sequences[i][0] += 1
                            default_config.sequences[i][cur_row] += 1
                        else:
                            pyautogui.click(cur_pos_minus[0], cur_pos_minus[1]+i*pos.seq_y_space)
                            default_config.sequences[i][cur_row] -= 1
                        time.sleep(click_wait)

            if config.sequences[i][2] != default_config.sequences[i][2]:
                if config.sequences[i][2] == -1:
                    pyautogui.click(pos.random_seq_items_pos[0], pos.random_seq_items_pos[1]+i*pos.seq_y_space)
                    default_config.sequences[i][2] = -1
                    time.sleep(click_wait)
                else:
                    while config.sequences[i][2] != default_config.sequences[i][2]:
                        if config.sequences[i][2] > default_config.sequences[i][2]:
                            pyautogui.click(pos.plus_seq_items_pos[0], pos.plus_seq_items_pos[1]+i*pos.seq_y_space)
                            default_config.sequences[i][2] += 1
                        else:
                            pyautogui.click(pos.minus_seq_items_pos[0], pos.minus_seq_items_pos[1]+i*pos.seq_y_space)
                            default_config.sequences[i][2] -= 1
                        time.sleep(click_wait)

        pyautogui.click(pos.edit_round_plus_pos)
        time.sleep(click_wait)


class GlobalConfig:
    def __init__(self):
        self.number_of_rounds = 3
        self.skip_intro = False
    def default():
        def_global_config = GlobalConfig()
        return def_global_config
    def enterConf(self):
        default_conf = GlobalConfig.default()
        
        if self.number_of_rounds != default_conf.number_of_rounds:
            while self.number_of_rounds != default_conf.number_of_rounds:
                if self.number_of_rounds > default_conf.number_of_rounds:
                    pyautogui.click(pos.plus_round_pos)
                    default_conf.number_of_rounds += 1
                else:
                    pyautogui.click(pos.minus_round_pos)
                    default_conf.number_of_rounds -= 1
                time.sleep(click_wait)
        
        if self.skip_intro:
            pyautogui.click(pos.intro_pos)
            time.sleep(click_wait)


class CompleteConfig:
    def __init__(self, json_file=None):
        self.global_config = GlobalConfig()
        self.round1_config = Config()
        self.round2_config = Config()
        self.round3_config = Config()
        if json_file:
            try:
                self.importFromJson(json_file)
            except FileNotFoundError:
                pass 

    def exportToJson(self, json_file='complete_config.json'):
        config_dict = {
            "global_config": self.global_config.__dict__,
            "round1_config": self.round1_config.__dict__,
            "round2_config": self.round2_config.__dict__,
            "round3_config": self.round3_config.__dict__
        }
        with open(json_file, 'w') as f:
            json.dump(config_dict, f, indent=4)

    def importFromJson(self, json_file):
        with open(json_file, 'r') as f:
            config_dict = json.load(f)
            self.global_config.__dict__.update(config_dict["global_config"])
            self.round1_config.__dict__.update(config_dict["round1_config"])
            self.round2_config.__dict__.update(config_dict["round2_config"])
            self.round3_config.__dict__.update(config_dict["round3_config"])
            
    def enterConf(self):
        for i in range(3):
            pyautogui.click(pos.edit_round_minus_pos)
            time.sleep(click_wait)

        pyautogui.click(pos.revert_changes_pos)
        time.sleep(click_wait)

        self.global_config.enterConf()

        if self.global_config.number_of_rounds == 1:
            self.round1_config.enterConf()
        elif self.global_config.number_of_rounds <= 2:
            self.round2_config.enterConf()
        elif self.global_config.number_of_rounds <= 3:
            self.round3_config.enterConf()

        pyautogui.click(pos.save_and_back_pos)
        time.sleep(click_wait)


class Pos:
    def __init__(self, target_res="1920x1080"):
        self.setRes(target_res)

    def set1920x1080(self):
        self.minus_round_pos = (270, 104)
        self.plus_round_pos = (330, 104)
        self.edit_round_minus_pos = (270, 155)
        self.edit_round_plus_pos = (330, 155)
        self.intro_pos = (270, 226)
        self.minus_starting_health_pos = (270, 276)
        self.plus_starting_health_pos = (320, 276)
        self.random_starting_health_pos = (370, 276)
        self.item_player_pos = (285, 445)
        self.item_table_pos = (325, 445)
        self.item_enabled_pos = (365, 445)
        self.item_y_space = 42
        self.minus_seq_blanks_pos = (1600, 190)
        self.plus_seq_blanks_pos = (1645, 190)
        self.random_seq_blanks_pos = (1690, 190)
        self.minus_seq_lives_pos = (1600, 236)
        self.plus_seq_lives_pos = (1645, 236)
        self.random_seq_lives_pos = (1690, 236)
        self.minus_seq_items_pos = (1600, 282)
        self.plus_seq_items_pos = (1645, 282)
        self.random_seq_items_pos = (1690, 282)
        self.seq_y_space = 212
        self.save_and_back_pos = (390, 970)
        self.revert_changes_pos = (390, 860)

    def setRes(self, target_res):
        self.set1920x1080()

        x, y = map(int, target_res.split('x'))
        scale_x = x / 1920
        scale_y = y / 1080

        for attr, val in list(self.__dict__.items()):
            if isinstance(val, tuple) and len(val) == 2:
                scaled_x = int(round(val[0] * scale_x))
                scaled_y = int(round(val[1] * scale_y))
                setattr(self, attr, (scaled_x, scaled_y))
        
        self.item_y_space = int(round(self.item_y_space * scale_y))
        self.seq_y_space = int(round(self.seq_y_space * scale_y))


def create_design_overlay(pos_obj, target_res_str):
    root = tk.Tk()
    
    w, h = map(int, target_res_str.split('x'))
    root.geometry(f"{w}x{h}")
    
    root.overrideredirect(True)
    root.attributes('-topmost', True)
    
    root.attributes('-type', 'dock')
    
    root.wait_visibility(root)
    
    canvas = tk.Canvas(root, width=w, height=h, highlightthickness=0)
    canvas.pack()
    
    root.attributes('-alpha', 0.7)

    def draw_dot(coord):
        if isinstance(coord, tuple) and len(coord) == 2:
            x, y = coord
            canvas.create_oval(x-5, y-5, x+5, y+5, fill='black', outline='')
            canvas.create_oval(x-3, y-3, x+3, y+3, fill='red', outline='')

    for attr, value in pos_obj.__dict__.items():
        if "pos" in attr:
            draw_dot(value)

    for i in range(9):
        draw_dot((pos_obj.item_player_pos[0], pos_obj.item_player_pos[1] + i * pos_obj.item_y_space))
        draw_dot((pos_obj.item_table_pos[0], pos_obj.item_table_pos[1] + i * pos_obj.item_y_space))
        draw_dot((pos_obj.item_enabled_pos[0], pos_obj.item_enabled_pos[1] + i * pos_obj.item_y_space))
        
    for i in range(4):
        draw_dot((pos_obj.random_seq_blanks_pos[0], pos_obj.random_seq_blanks_pos[1] + i * pos_obj.seq_y_space))
        draw_dot((pos_obj.plus_seq_blanks_pos[0], pos_obj.plus_seq_blanks_pos[1] + i * pos_obj.seq_y_space))
        draw_dot((pos_obj.minus_seq_blanks_pos[0], pos_obj.minus_seq_blanks_pos[1] + i * pos_obj.seq_y_space))
        draw_dot((pos_obj.random_seq_lives_pos[0], pos_obj.random_seq_lives_pos[1] + i * pos_obj.seq_y_space))
        draw_dot((pos_obj.plus_seq_lives_pos[0], pos_obj.plus_seq_lives_pos[1] + i * pos_obj.seq_y_space))
        draw_dot((pos_obj.minus_seq_lives_pos[0], pos_obj.minus_seq_lives_pos[1] + i * pos_obj.seq_y_space))
        draw_dot((pos_obj.random_seq_items_pos[0], pos_obj.random_seq_items_pos[1] + i * pos_obj.seq_y_space))
        draw_dot((pos_obj.plus_seq_items_pos[0], pos_obj.plus_seq_items_pos[1] + i * pos_obj.seq_y_space))
        draw_dot((pos_obj.minus_seq_items_pos[0], pos_obj.minus_seq_items_pos[1] + i * pos_obj.seq_y_space))

    exit_btn = tk.Button(root, text="Exit Design Mode", bg="#ff3333", fg="white", font=("Arial", 10, "bold"), command=root.destroy)
    canvas.create_window(w // 2, 30, window=exit_btn)

    root.mainloop()


global click_wait
click_wait = 0.005 

global pos
pos = Pos(target_res=TARGET_RESOLUTION)

if __name__ == "__main__":
    if EXECUTE_MODE == "design":
        create_design_overlay(pos, TARGET_RESOLUTION)
    else:
        config = CompleteConfig('edit_this_config.json')
        time.sleep(6)  
        config.enterConf()
