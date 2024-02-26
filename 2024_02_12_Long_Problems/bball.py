"""
File: bball.py
Author: Andy Siegel
Course: CSC 120, Spring 2024
Purpose: This python code takes in a file as input,
    and goes through every line creating team objects,
    puts them in a conference objects, and puts those 
    conferences in a conference set object. Then, the 
    code returns the conferences with the highest 
    winning percentage.
"""
class Team:
    """
    This class represents a basketball team and has the 
    attributes of its name, conference, wins, and losses. 
    """
    def __init__(self, line):
        team_info_list = line.split()
        team_info_dict = self.get_team_info_dict(team_info_list)
        self._team_name = team_info_dict['team_name']
        self._conference = team_info_dict['conference']
        self._wins = float(team_info_dict['wins'])
        self._losses = float(team_info_dict['losses'])

    def get_team_info_dict(self, info_list):
        """
        This function creates a dictionary containing 
        information about a team from a list.
        Args:
            info_list: a list of strings containing 
            information about the team
        Returns:
            A dictionary with the team's name, conference
            and wins and losses. 
        """
        team_info_dict = {}
        conf = []
        bracket_found = False
        end_index_of_name = 0
        # the conference is given by the final item in ()
        # begin by looping through the list backwards
        for element in info_list[::-1]:
            if ')' in element:
                # when the 'last' element with a ')' is found,
                # the boolean switches to true
                bracket_found = True
            if bracket_found:
                # all of the elements are added 
                # to the 'conf' list including the ends
                conf.append(element)
            if '(' in element:
                # when the closing '(' is found, the boolean
                # switches back to false, and the current
                # index is recorded (all of the following
                # items make up the name of the team)
                bracket_found = False
                end_index_of_name = info_list.index(element)
                break
        
        # because the list was looped through backwards, the conference
        # is flipped back so it is in readable format and the parentheses
        # are removed.
        team_info_dict['conference'] = ' '.join(conf[::-1]).strip('()')
        # the team name is from the first index to the index before the '('
        team_info_dict["team_name"] = ' '.join(info_list[0:end_index_of_name])
        team_info_dict['wins'] = info_list[-2]
        team_info_dict['losses'] = info_list[-1]

        return team_info_dict

    def name(self):
        return self._team_name
    
    def conf(self):
        return self._conference
    
    def win_ratio(self):
        """
        This function calculates the win ratio of a team.
        Parameters: none
        Returns:
            The ratio of wins to total games played.
        """
        ratio = self._wins / (self._wins + self._losses)
        return ratio

    
    def __str__(self):
        return f"{self.name()} : {self.win_ratio()}"

class Conference:
    def __init__(self, conf_name):
        self._name = conf_name
        self._teams = []
        self._sum_ratios = 0

    def __contains__(self, team):
        """
        This methods overrides the base 'in' operator
        when comparing a team and a conference
        Parameters:
            team: the team to check for against the
            conference represented by self
        Returns:
            True if the team is in the conference, 
            False otherwise
        """
        team_names_list = []
        for team_obj in self._teams:
            team_names_list.append(str(team_obj))
        for team_str in team_names_list:
            if team in team_str:
                return True
        return False


    def name(self):
        return self._name

    def add(self, team):
        """
        This function adds a new team to the list of teams
        and adds the overall win ratio so the average can 
        be returned in the future.
        Parameters:
            team: the team to be added
        Returns:
            None
        """
        self._teams.append(team)
        self._sum_ratios += team.win_ratio()


    def win_ratio_avg(self):
        """
        This function calculates the average win ratio of a team.
        Parameters:
            None
        Returns:
            The average win ratio of all teams in the conference
        """
        return (self._sum_ratios / len(self._teams))
    
    def __str__(self):
        return f"{self.name()} : {str(self.win_ratio_avg())}"

class ConferenceSet:
    def __init__(self):
        self._conferences = {}

    def add(self, conf): 
        self._conferences[conf.name()] = conf 

    def best(self):
        """
        This function returns a list of the best conferences 
        based on their win ratio averages.
        Parameters:
            None
        Returns:
            A list of conferences with the highest win ratio averages
        """
        conferences = list(self._conferences.values())

        best_win_ratios = []
        for conf in conferences:
            if len(best_win_ratios) == 0:
                best_win_ratios = [conf]

            elif conf.win_ratio_avg() > best_win_ratios[0].win_ratio_avg():
                best_win_ratios = [conf]
            elif conf.win_ratio_avg() == best_win_ratios[0].win_ratio_avg():
                best_win_ratios.append(conf)

        return best_win_ratios

    
def handle_input(file_name):
    """
    This function reads a file and creates a ConferenceSet 
    based on the data in the file.
    Args:
        file_name: the name of the file to be read
    Returns:
        A ConferenceSet object containing the data from the file
    """
    conference_set = ConferenceSet()
    file = open(file_name, 'r')
    for line in file:
        if '#' not in line:
            team = Team(line)
            if team.conf() not in conference_set._conferences:
                teams_conf = Conference(team.conf())
                teams_conf.add(team)
                conference_set.add(teams_conf)
            else:
                conference_set._conferences[team.conf()].add(team)

    return conference_set


def main():
    file_name = input()
    conference_set = handle_input(file_name)
    string_rep_confs = []
    for conf in conference_set.best():
        string_rep_confs.append(str(conf))
    for str_conf in sorted(string_rep_confs):
        print(str_conf)
    
main()