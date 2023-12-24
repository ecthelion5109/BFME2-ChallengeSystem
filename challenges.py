from datetime import datetime
from pathlib import Path
import pandas as pd
from icecream import ic

#---------------------------------------------------------------------#
"""----------------------------GLOBALS------------------------------"""
#---------------------------------------------------------------------#


#---------------------------#
CHALL_DATA_CSV = Path.cwd() / "chall_data.csv"


#---------------------------#
TOP_10_LEGACY = {
	#march 21 of 2021 by glute.
	10: "VITO",
	9: "DARYL",
	8: "TEMPT",
	7: "SCARECROW",
	6: "LAU",
	5: "IMPERIALIST",
	4: "AHWE",
	3: "OTTO",
	2: "SAURON",
	1: "ECTH",
}	


#---------------------------#
PLAYER_NAMES = {
	# "EOL_SCORP": ["Eol Scorpion"],
	# "APMN": ["Apmn"],
	# "SIBEL": ["SNOWBL4CK", "D3ATH^G0D"],
	"YUSUF": ["Yu$ufNi$ic"],
	"GANNICUS": ["Gannicus"],
	"THORIN": ["GranThorino", "thuren k-shild"],
	"RAINY": ["Rainy"],
	"HITMACHINE": ["HitMachine"],
	"YODA": ["Yoda", "PIO"],
	"NINKA": ["Recon|NinkaZy"],
	"KURDISH": ["KurdishBeg"],
	"NATHAN": ["Aow_NathanPearson"],
	"DOBBY": ["Dizz|Raptor", "Dobby"],
	"GOSPURE": ["GosPurePwneage", "Bilbo"],
	"MEWTWO": ["Mewtwo"],
	"PIKACHU": ["PiKaChu"],
	"MUSTAFA": ["King.Mustafa"],
	"JONES": ["Callan", "JonesBFME2"],
	"SAURON": ["S@uron"],
	"JEDGAR": ["J`Edgard"],
	"DARYL": ["Daryl"],
	"TEMPT": ["Temptation", "Lamma"],
	"VITO": ["Vito"],
	"OTTO": ["1.6 ArCh4Ng3L"],
	"ECTH": ["Eol Ecthelion"],
	"GLUTE": ["THE_GLUTE_MASTER"],
	"GRENDAL": ["TaR|Gr3ndal"],
	"MISHA": ["Vodishcka", "Cicus|Word"],
	"ANDY": ["AndyBrandy`"],
	"LOLO": ["Lothlorien"],
	"ENUMA": ["ENUMAra"],
	"AHWE": ["Ahwehawe"],
	"SCARECROW": ["Scare^Cr0w"],
	"FREEDOOM": ["FreeDooM"],
	"ZORBA": ["Imperious", "Zorbalator"],
	"MAKA": ["Maka`"],
	"LAU": ["Farmer Lau"],
	"IMPERIALIST": ["Imperialist"],
	"HALET": ["RECON|Halet"],
	"CASPER": ["Casper"],
	"LUXUS": ["AoW|LuXuS"],
}	


		

#---------------------------------------------------------------------#
"""-----------------------------CLASES-------------------------------"""
#---------------------------------------------------------------------#



#---------------------------#
class Player:
	# _last_played_chall_since_today = None
	def __init__(self, key, name):
		self.key = key
		self.name = name[0]
		self.rank = self.get_rank()
		self.cha_wins = 0
		self.cha_loses = 0
		self.challenges = []
		self.wins_total = 0
		self.wins1v1_total = 0
		self.wins2v2_total = 0
		
		self.games_played_total = 0
		self.games_played_1v1 = 0
		self.games_played_2v2 = 0
		
	@property	
	def loses_total(self):
		return self.games_played_total - self.wins_total
	@property	
	def loses_1v1_total(self):
		return self.games_played_1v1 - self.wins1v1_total
	@property	
	def loses2v2_total(self):
		return self.games_played_2v2 - self.wins2v2_total
	
	@property	
	def fecha_de_alta(self):
		# if hasattr
		# return sorted([cha for cha in self.challenges], key=lambda x: x.index)[0]
		return self.challenges[0]
		
	# @property	
	# def last_played_chall(self):
		# real_challenges = sorted([cha for cha in self.challenges if cha.is_cha], key=lambda x: x.index)
		# real_challenges = sorted([cha for cha in self.challenges if cha.is_cha], key=lambda x: x.index)
		# print(real_challenges)
		# return self.challenges[-1].date
		# if real_challenges:
			# self.last_challenge = real_challenges[-1]
			# return real_challenges[-1].date
		# else:
			# return None #"Never" # self.challenges[0].date
		
	# @property	
	# def from_today_days_since_last_chall(self):
		# if True:
		# if self._last_played_chall_since_today is None:
			# last_cha = self.last_played_chall()
			# if last_cha is None:
				# return "Never"
			# else:
				# last_cha = round(((datetime.today() - self.last_played_chall()).days / 30), 2)
				# self._last_played_chall_since_today = last_cha
			
		# return self._last_played_chall_since_today
			
	# def last_played_chall_since_today_string(self):	
		# last_cha = self.last_played_chall()
		# if last_cha:
			# delta = round(((datetime.today() - self.last_played_chall()).days / 30), 2)
			# return f"{self.name} has not played a challenge since {delta} months"
		# else:
			# return None
		
	def is_black(self):
		return True if self.key in {PLAYERS["ANDY"].key, PLAYERS["LAU"].key} else False
		
	def cha_winrate(self):
		if self.cha_wins == 0:
			return 0
		total_matches = self.cha_wins + self.cha_loses
		assert total_matches == len(self.challenges)
		return (self.cha_wins / total_matches) * 100.0
		
		
	def get_1v1_vs(self, other, printEm=True):
		listt = [chall for chall in self.challenges if (chall.p1.history is self or chall.p2.history is self) and (chall.p1.history is other or chall.p2.history is chall)]
		self_wins = len({a for a in listt.values() if a.winner.history is self})
		other_wins = len({a for a in listt.values() if a.winner.history is other})
		total_matches = len(listt)
		if total_matches == 0:
			winrate = 0
		else:
			winrate = (self_wins / total_matches) * 100.0
		if printEm:
			print(f"{self.name} vs {other.name}: {self_wins}-{other_wins} | WinRate: {winrate}")
		else:
			if total_matches > 0:
				return self_wins > other_wins 
			else:
				return None
		
	def __gt__(self, other):
		bol = self.get_1v1_vs(other, printEm=False)
		if bol is None:
			bol = self.cha_winrate()  > other.cha_winrate()
		print(f"{self.key} better than {other.key} = {bol}")
		return bol
		
	def update_match_history(wins1v1, wins2v2, loses1v1, loses2v2):
		self.wins1v1 = wins1v1
		self.wins2v2 = wins2v2
		self.loses1v1 = loses1v1
		self.loses2v2 = loses2v2
		self.wins = wins1v1 + wins2v2
		self.loses = loses1v1 + loses2v2
		
	def get_rank(self):
		inverted_dict = {value: key for key, value in TOP_10_LEGACY.items()}
		rank = inverted_dict.get(self.key, None)
		if rank is None:
			rank = len(TOP_10_LEGACY)+1
			TOP_10_LEGACY[rank] = self.key
		return rank
		
	def __str__(self):
		return f"|{self.key}|\tRank:{self.rank}\t|Wins:{self.cha_wins}|Loses:{self.cha_loses}"
	def __repr__(self):
		return f"|{self.key}|\tRank:{self.rank}\t|Wins:{self.cha_wins}|Loses:{self.cha_loses}"

#---------------------------#
class Challenge:
	_str_add_and_kick_or_none = None
	_str_score1v1 = None
	_str_score2v2 = None
	_str_scoreTotal_or_none = None
	_str_defended_or_took_over = None
	_str_version_or_no_score = None
	_str_undefended_or_not = None
	_str_challenge_or_none = None
	_str_bo9_or_b4b5 = None
	#---------------------------#
	class PlayerInChallenge:
		_last_challenge = None
		_days_since_last_chall = None
		def __init__(self, master, key, wins1v1, wins2v2):
			self.key = key
			self.master = master
			self.wins1v1 = wins1v1
			self.wins2v2 = wins2v2
			self.wins = wins1v1 + wins2v2
			self.history = PLAYERS[key]
			self.history.challenges.append(master)
			self.rank = self.history.rank
			
		@property
		def rank_ordinal(self):
			ORDINAL = {
				1: "1st",
				2: "2nd",
				3: "3rd",
				4: "4th",
				5: "5th",
				6: "6th",
				7: "7th",
				8: "8th",
				9: "9th",
				10: "10th"
			}
			return ORDINAL.get(self.rank, "from outside the list")
			# return ORDINAL[self.rank]
			
		@property
		def last_challenge(self):
			if self._last_challenge is None:
				self._last_challenge = self.history.challenges[-2]
			return self._last_challenge
		
			
		@property
		def days_since_last_chall(self):	
			if self._days_since_last_chall is None:
				if self.last_challenge is None:
					self._days_since_last_chall = None # self.history.fecha_de_alta.date
				else:
					delta = self.master.date - self.last_challenge.date
					self._days_since_last_chall = delta.days # /30
			return self._days_since_last_chall
			
		def __repr__(self):
			return f"|{self.history.key}|"
	#---------------------------#
	def __init__(self, index, row):
		self.index = index
		self.version = row["version"]
		self.date = datetime.strptime(row["date"], '%Y-%m-%d')
		self.dateString = datetime.strptime(row["date"], '%Y-%m-%d').strftime('%Y-%m-%d')
		self.dont_score_mode = self.version == "NO_SCORE"
		self.is_add_and_kick = self.version == "ADD_AND_KICK"
		if not self.dont_score_mode and not self.is_add_and_kick:
			player1 = Challenge.PlayerInChallenge(self, row["p1"], row["p1wins1v1"], row["p1wins2v2"])
			player2 = Challenge.PlayerInChallenge(self, row["p2"], row["p2wins1v1"], row["p2wins2v2"])
			self.winner = player2 if player2.wins > player1.wins else player1
			self.loser = player1 if self.winner == player2 else player2
		else:
			player1 = Challenge.PlayerInChallenge(self, row["p1"], 0, 0)
			player2 = Challenge.PlayerInChallenge(self, row["p2"], 0, 0)
			self.winner = player1 
			self.loser = player2 
		self.games_total = self.winner.wins + self.loser.wins
		self.games1v1 = self.winner.wins1v1 + self.loser.wins1v1
		self.games2v2 = self.winner.wins2v2 + self.loser.wins2v2
		
			
		self.challenger = player1 if player1.rank > player2.rank else player2
		self.defender = player1 if self.challenger == player2 else player2
		self.everyone_else_on_list = {player for player in PLAYERS.values() if player.key not in {self.winner.key, self.loser.key}}
		self.custom_msg = f"\n\n\tComment: {row['message']}" if row['message'] else ""
		self.flawless = "flawlessly " if self.loser.wins == 0 and not self.dont_score_mode and not self.is_add_and_kick else ""
		
		if self.dont_score_mode:
			self.update_histories(issue_score=False)
		elif self.str_add_and_kick_or_none:
			self.add_p1_kick_p2()
		elif self.games_total:
			self.update_histories(issue_score=True)	
			
		self.top10 = self.save_current_top_10()
		self.disputed_rank = self.defender.rank
		
		
	
	@property
	def is_cha(self):
		return not self.str_add_and_kick_or_none and not self.dont_score_mode
		
		
		
	def add_p1_kick_p2(self):
		last_spot = len(PLAYERS)
		if self.winner.rank > self.loser.rank:
			for player in self.everyone_else_on_list:
				if player.rank > self.winner.rank:
					player.rank -= 1
				if player.rank > self.loser.rank and player.rank < 11:
					player.rank -= 1
			self.winner.history.rank = 10 
			self.loser.history.rank += last_spot # 
		
	def save_current_top_10(self):
		top_10_as_dict = {
			player.rank: player
			for player in PLAYERS.values()
			if 1 <= player.rank <= 10
		}
		as_string = "\t\tTOP 10\n"
		for rank, player in sorted(top_10_as_dict.items(), reverse=True):
			as_string += f"\t{rank:<4}. {player.name:20} {player.cha_wins}-{player.cha_loses}\n"
		return as_string
			
	def __repr__(self):
		return f"|Cha{self.index}|{self.version}|{self.winner}{self.winner.wins}|{self.loser}{self.loser.wins}|"
		
	@property
	def str_score1v1_or_none(self):
		if self._str_score1v1 is None:
			if self.games1v1:
				self._str_score1v1 = f"\nScore 1vs1: {self.winner.wins1v1}-{self.loser.wins1v1} for {self.winner.history.name}"
			else:
				self._str_score1v1 = ""
		return self._str_score1v1
		
	@property
	def str_score2v2_or_none(self):
		if self._str_score2v2 is None:
			if self.games2v2:
				self._str_score2v2 = f"\nScore 2vs2: {self.winner.wins2v2}-{self.loser.wins2v2} for {self.winner.history.name}"
			else:
				self._str_score2v2 = ""
		return self._str_score2v2
		
	@property
	def str_scoreTotal_or_none(self):
		if self._str_scoreTotal_or_none is None:
			if self.games2v2:
				self._str_scoreTotal_or_none = f"\nScore: {self.winner.wins}-{self.loser.wins} for {self.winner.history.name}" if self.games2v2 else ""
			else:
				self._str_scoreTotal_or_none = ""
		return self._str_scoreTotal_or_none
		
	@property
	def str_undefended_or_not(self):
		if self._str_undefended_or_not is None:
			if self.dont_score_mode:
				self._str_undefended_or_not = f"\nSpotUndefended: {self.defender.history.name} has not shown any activity in a week nor has attempted to arrange a play-date to defend his spot."
			else:
				self._str_undefended_or_not = ""
		return self._str_undefended_or_not
		
	@property
	def str_add_and_kick_or_none(self):
		if self._str_add_and_kick_or_none is None:
			if self.is_add_and_kick:
				since_last_event = f'Since Challenge{self.defender.last_challenge.index}' #if self.defender.last_challenge else f'Since added in the top10 list in the ChallengeEvent{self.defender.fecha_de_alta}'
				self._str_add_and_kick_or_none = f"{f"\n\nAddAndKickUpdate: {since_last_event}, {self.defender.history.name} has not played any game or challenge in {self.defender.days_since_last_chall} days."}{f"\n\n- {self.defender.history.name} has been kicked from the {self.defender.rank_ordinal} spot and from the list." }"
			else:
				self._str_add_and_kick_or_none = ""
		return self._str_add_and_kick_or_none
		
	@property
	def str_defended_or_took_over(self):
		if self._str_defended_or_took_over is None:
			if self.is_add_and_kick:
				self._str_defended_or_took_over = f"\n\n+ {self.challenger.history.name} has been added to the top10 list, begining on the 10th spot."
			else:
				if self.defender is self.winner:
					self._str_defended_or_took_over = f"\n\n+ {self.defender.history.name} has {self.flawless}defended the {self.defender.rank_ordinal} spot!"
				else:
					self._str_defended_or_took_over = f"\n\n+ {self.challenger.history.name} has {self.flawless}took over the {self.defender.rank_ordinal} spot!" 
		return self._str_defended_or_took_over
		
	@property
	def str_version_or_no_score(self):
		if self._str_version_or_no_score is None:
			if self.games_total:
				self._str_version_or_no_score = f"\n\nGames were played in {self.version}"
			else:
				self._str_version_or_no_score = "\n\nNo wins or loses have been scored."
		return self._str_version_or_no_score
		
	
	@property
	def str_bo9_or_b4b5(self):
		if self._str_bo9_or_b4b5 is None:
			if not self.games2v2:
				# self._str_bo9_or_b4b5 = "Challenge Mode: Best of 9 in 1vs1."
				self._str_bo9_or_b4b5 = ""
			else:
				self._str_bo9_or_b4b5 = "\nMode: Traditional challenge (4 games as 2vs2, 4 games as 1vs1, untie with 1vs1)."
		return self._str_bo9_or_b4b5
		
		
		
		
		
	@property
	def str_challenge_or_none(self):
		if self._str_challenge_or_none is None:
			if not self.is_add_and_kick: #self.is_cha:
				self._str_challenge_or_none = f"\n\n{self.challenger.history.name} ({self.challenger.rank_ordinal}) has challenged {self.defender.history.name} ({self.defender.rank_ordinal}) for his spot.{self.str_bo9_or_b4b5} "
			else:
				self._str_challenge_or_none = ""
		return self._str_challenge_or_none
		
		
		
		
		
	def __str__(self):
		return f"\n------------------------------------\nChallenge{self.index}_{self.challenger.history.key} vs {self.defender.history.key}, {self.challenger.wins}-{self.defender.wins}, {self.version}\n```diff\n\n- Challenge № {self.index}\n- Update {self.dateString}{self.str_challenge_or_none}\n{self.str_score1v1_or_none}{self.str_score2v2_or_none}{self.str_scoreTotal_or_none}{self.str_undefended_or_not}{self.str_add_and_kick_or_none}{self.str_defended_or_took_over}{self.custom_msg}{self.str_version_or_no_score}\n\nLet the challenges continue!\n\n{self.top10}```"
		
	def update_histories(self, issue_score):
		if self.winner.history.rank > self.loser.history.rank:
			for player in self.everyone_else_on_list:
				if player.rank > self.winner.history.rank:
					player.rank -= 1
				if player.rank > self.loser.history.rank:
					player.rank += 1
			self.winner.history.rank = self.loser.history.rank
			self.loser.history.rank += 1
		if issue_score:
			self.winner.history.cha_wins += 1
			self.loser.history.cha_loses += 1
				
			
			self.winner.history.games_played_total += self.games_total
			self.winner.history.games_played_1v1 += self.games1v1
			self.winner.history.games_played_2v2 += self.games2v2
			self.winner.history.wins_total += self.winner.wins
			self.winner.history.wins1v1_total += self.winner.wins1v1
			self.winner.history.wins2v2_total += self.winner.wins2v2
			
			self.loser.history.games_played_total += self.games_total
			self.loser.history.games_played_1v1 += self.games1v1
			self.loser.history.games_played_2v2 += self.games2v2
			self.loser.history.wins_total += self.loser.wins
			self.loser.history.wins1v1_total += self.loser.wins1v1
			self.loser.history.wins2v2_total += self.loser.wins2v2
		


#---------------------------------------------------------------------#
"""---------------------------FUNCIONES------------------------------"""
#---------------------------------------------------------------------#


#---------------------------#
def dataframe_01_readear(archivo):
	CABECERAS = ['chall','version','p1','p1wins1v1','p1wins2v2','p2','p2wins1v1','p2wins2v2','date']
	INDICE = 'chall'
	if archivo.exists() and archivo.stat().st_size >0 :
		data = pd.read_csv(
			filepath_or_buffer = archivo, 
			sep = ";", 
			# decimal = ",", 
			encoding = "latin1",
			index_col = INDICE,
			dtype={'version': str}
		)
		# data.set_index(INDICE, inplace=True)
	else:
		data = pd.DataFrame(columns=CABECERAS)
		data.set_index(INDICE, inplace=True)
		
	data.sort_index(inplace=True, ascending=True)
	# data.sort_values(by='chall', inplace=True)
	# data.sort_index(inplace=True)
	data = data.map(lambda x: x.strip() if isinstance(x, str) else x)
	data['message'].fillna('', inplace=True)
	return data
		
def write_csv(data, archivo, reverse=False):
	# data["chall"] = data.index + 1
	# data.set_index("chall", inplace=True)
	if reverse:
		data.sort_index(inplace=True, ascending=False)
	data.to_csv(
		path_or_buf = archivo, 
		sep = ";", 
		index = True,
		decimal = ",", 
		encoding = "latin1"
	)
	print(".csv guardado.")
		

#---------------------------#
def print_01_challenge_log(reverse=False):
	sorted_dict = {key: CHALLENGES[key] for key in sorted(CHALLENGES, reverse=reverse)}
	for cha in sorted_dict.values():
		print(cha)
		
def write_chalog(reverse=True):
	sorted_dict = {key: CHALLENGES[key] for key in sorted(CHALLENGES, reverse=reverse)}
	super_string = f"##AutoGenerated by 'challenges.py' {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}\nRegards, Bambi\n\n"
	for cha in sorted_dict.values():
		super_string += str(cha)
	with open("challenges.log", "w", encoding='utf-8') as file:
		file.write(super_string)
	
	
		
# def print_02_sorted_players_by_activity():
	# sorted_players = list(sorted(PLAYERS.values(), key=lambda player: player.from_today_days_since_last_chall))

	# ordered_player_dict = {player.name: player.from_today_days_since_last_chall for player in sorted_players}
	# dictt = {player.key: player.from_today_days_since_last_chall for player in sorted_players}
	# ic(sorted_players)
		
def print_03_player_vs_player():
	PLAYERS["ECTH"].get_1v1_vs(PLAYERS["MISHA"], printEm=True)
	PLAYERS["ECTH"].get_1v1_vs(PLAYERS["OTTO"], printEm=True)
	PLAYERS["ECTH"].get_1v1_vs(PLAYERS["SAURON"], printEm=True)
	PLAYERS["ECTH"].get_1v1_vs(PLAYERS["ANDY"], printEm=True)
	PLAYERS["ECTH"].get_1v1_vs(PLAYERS["AHWE"], printEm=True)

	PLAYERS["MISHA"].get_1v1_vs(PLAYERS["OTTO"], printEm=True)
	PLAYERS["MISHA"].get_1v1_vs(PLAYERS["ANDY"], printEm=True)
	PLAYERS["MISHA"].get_1v1_vs(PLAYERS["SAURON"], printEm=True)

	PLAYERS["OTTO"].get_1v1_vs(PLAYERS["ANDY"], printEm=True)
	PLAYERS["OTTO"].get_1v1_vs(PLAYERS["NATHAN"], printEm=True)
	PLAYERS["OTTO"].get_1v1_vs(PLAYERS["LUXUS"], printEm=True)
	PLAYERS["OTTO"].get_1v1_vs(PLAYERS["SAURON"], printEm=True)
	PLAYERS["OTTO"].get_1v1_vs(PLAYERS["AHWE"], printEm=True)
	
def print_04_who_is_black():
	ic(PLAYERS["ECTH"].is_black())
	ic(PLAYERS["LAU"].is_black())
	ic(PLAYERS["ANDY"].is_black())
#---------------------------#
		

#---------------------------------------------------------------------#
"""-----------------------------CLASES-------------------------------"""
#---------------------------------------------------------------------#


if __name__ == "__main__":
	"""1. Instance PlayerHistory Objects"""
	PLAYERS = {
		key: Player(key, name) 
		for key, name 
		in PLAYER_NAMES.items()
	}
	# ic(PLAYERS)

	"""2. Read csv"""
	data = dataframe_01_readear(CHALL_DATA_CSV)	
	# print(data)
	
	
	"""3. Update csv"""
	# write_csv(data, CHALL_DATA_CSV, reverse=True)

	"""4. Instance Challenge Objects"""
	CHALLENGES = {	
		index: Challenge(index, row)
		for index, row 
		in data.iterrows()
	}

	"""5. Testing functions"""
	write_chalog(reverse=True)
	
	"""4. Testing functions"""
	# print_01_challenge_log(reverse=False)
	# print_02_sorted_players_by_activity()
	# print_03_player_vs_player()
	# print_04_who_is_black()
	
# ic(
# PLAYERS["SAURON"].wins2v2_total, PLAYERS["SAURON"].loses2v2_total, 
# PLAYERS, 
# )

