#include "myStuff.hpp"
#include "nlolhmannJson.hpp"
#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <fstream>
#include <cstdlib> // Required for system()
#include <sstream>
#include <stdexcept>
#include <algorithm>
#include <functional>

// using json = nlohmann::json;
using namespace myStuff;
using namespace nlohmann;
using namespace std;

// Example usage
// int number = get_int("Ingrese un número (1-10): ", 0, true, 1, 10);
// cout << "Número ingresado: " << number << "\n";

// bool decision = get_boolean("¿Desea continuar?", 'S', 'N', 0);
// cout << "Decisión: " << (decision ? "Sí" : "No") << "\n";

/*---------------------------------------------------
---------------------ok. declaraciones-------------
----------------------------------------------------*/


class PlayerHistory;
class ChallengeEvent;
class PlayerInChallenge;
class ChallengeSystem;














/*---------------------------------------------------
------------------PlayerInChallenge.Class.03-----------
----------------------------------------------------*/


class PlayerInChallenge{
  public:
	ChallengeEvent& challenge;
	// PlayerHistory& history;
	string key;
	int wins1v1;
	int wins2v2;
	int wins;
		// rank = challenge.chasys._get_index_or_append_if_new(self.history);
		  // history(challenge.chasys.PLAYERS.at(key)),
	
	// Constructor
	PlayerInChallenge(ChallengeEvent& challenge, string key, string wins1v1, string wins2v2) 
	: 	challenge(challenge), 
		key(key),
		wins1v1(stoi(wins1v1)), 
		wins2v2(stoi(wins2v2)) {
		wins = this->wins1v1 + this->wins2v2;
	}
	// ###----------------PlayerInChallenge.Methods-------------###
	
	// ###----------------PlayerInChallenge.Properties-------------###
	// ###--------------------PlayerInChallenge.Dunder.Methods----------------###
	
	string repr(){
		ostringstream oss;
		oss << "|"
			<< key 
			<< "|wins1v1:" 
			<< wins1v1 
			<< "|wins2v2:" 
			<< wins2v2 
			<< "|total" 
			<< wins 
			<< "|";
		return oss.str();
		
	}

};







/*---------------------------------------------------
------------------ChallengeEvent.Class.02-----------
----------------------------------------------------*/

class ChallengeEvent{
  public:
	ChallengeSystem& chasys;
	int key = key;
	string version;
	// date = datetime.strptime(row["date"], '%Y-%m-%d')
	string fecha;
	string notes;
	PlayerInChallenge winner;
	PlayerInChallenge loser;
	string top10string;
		
	// Constructor
	ChallengeEvent(ChallengeSystem& chasys, int key, map<string, string> row)
		: 	chasys(chasys), 
			key(key),
			version(row.at("version")),
			fecha(row.at("date")),
			notes(row["notes"]), // Not all challenges have notes, in that case, create an empty string.
			winner(PlayerInChallenge(*this, row.at("w_key"), row.at("w_wins1v1"), row.at("w_wins2v2"))),
			loser(PlayerInChallenge(*this, row.at("l_key"), row.at("l_wins1v1"), row.at("l_wins2v2")))
		{
		// _init_01_integrity_check()
		// _init_02_impact_players_historial()
		// _init_03_impact_system_top10_rank()
		// top10string = self.__get_top10string()
		// __build_top10string();
	}
	
	
	
	// void __build_top10string(){
		// top10string = "\t\tTOP 10\n";
		// for (size_t i = chasys.TOP_OF; i > 0; i--){
			// if (i >= chasys.top10list.size()){
				// continue;
			// }
			// auto& player = chasys.top10list[i];
			
			// ostringstream pre_string;
			// pre_string << "\t" << setw(4) << left << (i + 1) << ". "
				// << setw(20) << left << player.name
				// << player.cha_wins << "-" << player.cha_loses << "\n";

			// Append to the top10string
			// top10string.append(pre_string.str());
		// }
	// }
	
	
		
	string replays_dir() {
		ostringstream oss;

		// Concatenate the string components
		// oss << chasys.chareps
		oss << "\\Challenge"
			<< key 
			<< "_"
			<< winner.key
			<< "_vs_"
			<< loser.key
			<< ",_"
			<< winner.wins
			<< "-"
			<< loser.wins
			<< ",_"
			<< version
			<< ".rar";
		return oss.str();
	}
	string repr(){
		ostringstream oss;
		oss << "|" << key << "|" << version << "\tWinner: " << winner.repr() << "\tLoser: " << loser.repr() << "\n";
		return oss.str();
		
	}
	
	string str(){
		ostringstream oss;
		oss << "------------------------------------\n"
			<< replays_dir() 
			<< "\n"
			<< "```diff\n"
			<< "\n- Challenge № "
			<< key
			<< "\n- Update "
			<< fecha
			<< "\nNotes: "
			<< notes
			// << _04_get_my_report()
			<< "\n\nLet the challenges continue!\n\n"
			<< top10string
			<< "```";
		return oss.str();
	}
	
	//###--------------------ChallengeEvent.Private.Methods-------------###

	
	// ###--------------------ChallengeEvent.Static.Methods-------------###

	// ###--------------------ChallengeEvent.Public.Methods-------------###

	// ###--------------------ChallengeEvent.Protected.Methods-------------###

	//###--------------------ChallengeEvent.Private.Methods-------------###

		
	//--------------------ChallengeEvent.Properties-------------###
	

};












/*---------------------------------------------------
------------------PlayerHistory.Class.01-----------
----------------------------------------------------*/
class PlayerHistory {
  public:
	ChallengeSystem& chasys;
	string key;
	vector<string> names;
	int cha_wins = 0;
	int cha_loses = 0;
  
	// Constructor
	PlayerHistory(ChallengeSystem& chasys, const string& key, const json& value) 
		:	chasys(chasys), 
			key(key),
			names(read_nicknames(value["nicknames"]))
				
		{
	}
	
	string repr(){
		ostringstream oss;
		oss << "|" << key << "|\t|Wins:" << cha_wins << "|Loses:" << cha_loses;
		return oss.str();
	}
	
  private:
	vector<string> read_nicknames(const json& names_array){
		vector<string> nicknames;
		for (const auto& nickname : names_array) {
			nicknames.push_back(nickname.get<string>());
		}
		return nicknames;
	}
};
	
	
	
	
/*---------------------------------------------------
------------------ChallengeSystem.Class.04-----------
----------------------------------------------------*/
class ChallengeSystem {
  public:
	int TOP_OF = 9;
	string chareps;
	string chacsv;
	string chalog;
	string status;
	string webhook_url;
	map<string, PlayerHistory> PLAYERS;
	vector<PlayerHistory*> top10list;
	map<int, ChallengeEvent> CHALLENGES;
	
	// Constructor
	ChallengeSystem(const string& chareps, const string& chacsv, const string& chalog, const string& status, const string& webhook_url, const json player_data)
		:	chareps(chareps), 
			chacsv(chacsv), 
			chalog(chalog), 
			status(status), 
			webhook_url(webhook_url), 
			PLAYERS(read_PLAYERS(player_data["active_players"])),
			top10list(read_LEGACY(player_data["legacy"]["top10"])),
			CHALLENGES(read_CHALLENGES(chacsv))
	{
		// show_players();
		// show_top10();
		
		write_chalog();
	}
	
	void write_chalog() {
		string super_string = "##AutoGenerated by 'ChallengeSystem'\nRegards, Bambi\n\n";

		for (auto& pair : CHALLENGES) {
			auto& key = pair.first;
			auto& challenge = pair.second; 
			super_string.append(challenge.str());
		}

		// Open the file with the name stored in the chalog variable
		ofstream file(chalog); // This will open the file specified by 'chalog'

		if (file.is_open()) {
			file << super_string;
			file.close();
			cout << "* " << chalog << " was updated" << endl;
		} else {
			cout << "Error: Could not open file " << chalog << endl;
		}

		cout << ".chalog guardado." << endl;
	}
	
	void show_players() {
		for (auto& pair : PLAYERS) {
			auto& key = pair.first;
			auto& player = pair.second; 
			cout << key << " : " << player.repr() << endl;
		}
	}
	
	void show_challenges() {
		for (auto& pair : CHALLENGES) {
			auto& key = pair.first;
			auto& challenge = pair.second; 
			// cout << key << " : " << challenge.repr() << endl;
			cout << key << " : " << challenge.str() << endl;
		}
	}
	
	void show_top10() {
		for (size_t i = 0; i < top10list.size(); i++) {
			cout << i + 1 << " : " << top10list[i]->repr() << endl;
		}
	}
	
  private:
	// ###----------------ChallengeSystem.Private.Methods------------###
	 map<int, ChallengeEvent> sortedDictOfChallFromLines (const vector<string>& lines) {
		vector<string> headers;
		vector<vector<string>> rows;

		// cout << "11, sortedDictOfChallFromLines" << endl;
			
		// Parse headers
		istringstream headerStream(lines[0]);
		string header;
		while (getline(headerStream, header, ';')) {
			headers.push_back(header);
		}

		// Parse rows
		for (size_t i = 1; i < lines.size(); ++i) {
			vector<string> row;
			istringstream rowStream(lines[i]);
			string cell;
			while (getline(rowStream, cell, ';')) {
				row.push_back(cell);
			}
			rows.push_back(row);
		}

		// Sort rows by the "key" column (assume column 0)
		sort(rows.begin(), rows.end(), [](const vector<string>& a, const vector<string>& b) {
			return stoi(a[0]) < stoi(b[0]);
		});

		// Build map of key to ChallengeEvent
		map<int, ChallengeEvent> dataaaa;
		for (const auto& row : rows) {
			map<string, string> rowDict;
			for (size_t j = 0; j < headers.size(); ++j) {
				if (j < row.size()) {
					rowDict[headers[j]] = row[j];
				}
			}
			
			// cout << "22, DEBUG" << endl;
			// Extract the key and version
			int key = stoi(rowDict.at("key"));
			// string version = rowDict.at("version");

			// cout << "33, DEBUG" << endl;
			// Create the ChallengeEvent and add it to the map
			
			// print_map_and_wait(rowDict);
			
			dataaaa.emplace(key, ChallengeEvent(*this, key, rowDict));
			
			// cout << "44, success instancing ChallengeEvent" << endl;
		}
		return dataaaa;
	};
	
	
	map<int, ChallengeEvent> read_CHALLENGES(string csv_file_path){
        ifstream file(csv_file_path, ios::in);
        if (!file.is_open() || file.peek() == ifstream::traits_type::eof()) {
            throw runtime_error("No existe " + csv_file_path);
        }

		// Read lines
		vector<string> lines;
		string line;
		while (getline(file, line)) {
			lines.push_back(line);
		}
		
        return sortedDictOfChallFromLines(lines);
	}
	
	
	map<string, PlayerHistory> read_PLAYERS(json active_players){
		map<string, PlayerHistory> players_map;
		for (auto it = active_players.items().begin(); it != active_players.items().end(); ++it) {
			players_map.emplace(it.key(), PlayerHistory(*this, it.key(), it.value()));
		}
		return players_map;
	}
	
	vector<PlayerHistory*> read_LEGACY(json legacy_top10){
		vector<PlayerHistory*> top10vector;
		for (int i = 0; i < legacy_top10.size(); i++){
			string player_key = legacy_top10[i];
			top10vector.push_back(&PLAYERS.at(player_key));
			
			
		}
		return top10vector;
	}
};

		
/*---------------------------------------------------
------------------ok.Iniciar-------------------------
----------------------------------------------------*/
int main() {
	// ChallengeSystem sistema;
    ChallengeSystem* sistema = nullptr;
	try {
		// Instantiate ChallengeSystem
		sistema = new ChallengeSystem(
			"..\\replays",
			"..\\data\\challenges.csv",
			// "..\\output\\challenges.log",
			"challenges.log",
			"..\\output\\status.log",
			"https://discord.com/api/webhooks/840359006945935400/4Ss0lC1i2NVNyZlBlxfPhDcdjXCn2HqH-b2oxMqGmysqeIdjL7afF501gLelNXAe0TOA",
			json::parse(readFile("..\\data\\players.json"))
		);
		
	} catch (const exception& e) {
		cerr << "Error: " << e.what() << endl;
	}
	// sistema->show_players();
	// sistema->show_top10();
	// sistema->show_challenges();
	system("pause");
	

	return 0;
}