import statistics
import app.database.repository.mission_repository as mission_repos



def get_mission_stats_by_city(city: str):
    missions = mission_repos.get_mission_by_city(city)
    avg = statistics.mean([mission.target[0].target_priority or 0 for mission in tuple(missions)])
    return {"mission_count": len(missions), "avg_priority_points":avg}