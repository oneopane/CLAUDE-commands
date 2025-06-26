#!/usr/bin/env python3
"""
Graph visualizer for Linear workflow
Converts JSON dependency graphs to Mermaid diagrams
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Set, Tuple

class GraphVisualizer:
    def __init__(self, graph_path: str):
        with open(graph_path, 'r') as f:
            self.graph = json.load(f)
        self.nodes = self.graph.get('nodes', {})
        self.edges = self.graph.get('edges', [])
    
    def generate_mermaid(self, view_type: str = 'full') -> str:
        """Generate Mermaid diagram based on view type"""
        if view_type == 'full':
            return self._generate_full_graph()
        elif view_type == 'critical':
            return self._generate_critical_path()
        elif view_type == 'status':
            return self._generate_status_view()
        else:
            return self._generate_full_graph()
    
    def _generate_full_graph(self) -> str:
        """Generate complete graph with all nodes and edges"""
        lines = ['graph TD']
        
        # Group nodes by parent
        groups = self._group_by_parent()
        
        # Generate subgraphs
        for parent_id, children in groups.items():
            if parent_id:
                parent = self.nodes.get(parent_id, {})
                lines.append(f'    subgraph "{parent.get("title", "Unknown")}"')
                for child_id in children:
                    lines.append(f'        {self._node_line(child_id)}')
                lines.append('    end')
            else:
                # Root level items
                for child_id in children:
                    lines.append(f'    {self._node_line(child_id)}')
        
        # Add edges
        for edge in self.edges:
            if edge['type'] != 'contains':  # Skip parent-child edges
                lines.append(f'    {self._edge_line(edge)}')
        
        return '\n'.join(lines)
    
    def _generate_critical_path(self) -> str:
        """Show only blocking dependencies"""
        lines = ['graph TD']
        blocking_edges = [e for e in self.edges if e['type'] == 'blocks']
        critical_nodes = set()
        
        for edge in blocking_edges:
            critical_nodes.add(edge['from'])
            critical_nodes.add(edge['to'])
        
        for node_id in critical_nodes:
            lines.append(f'    {self._node_line(node_id)}')
        
        for edge in blocking_edges:
            lines.append(f'    {self._edge_line(edge)}')
        
        return '\n'.join(lines)
    
    def _generate_status_view(self) -> str:
        """Group by status"""
        lines = ['graph TD']
        status_groups = {}
        
        for node_id, node in self.nodes.items():
            status = node.get('status', 'unknown')
            if status not in status_groups:
                status_groups[status] = []
            status_groups[status].append(node_id)
        
        for status, node_ids in status_groups.items():
            lines.append(f'    subgraph "{status.title()}"')
            for node_id in node_ids:
                lines.append(f'        {self._node_line(node_id)}')
            lines.append('    end')
        
        for edge in self.edges:
            if edge['type'] != 'contains':
                lines.append(f'    {self._edge_line(edge)}')
        
        return '\n'.join(lines)
    
    def _node_line(self, node_id: str) -> str:
        """Generate line for a single node"""
        node = self.nodes.get(node_id, {})
        title = node.get('title', 'Unknown')
        status = node.get('status', 'pending')
        node_type = node.get('type', 'issue')
        
        # Status emoji
        status_emoji = {
            'completed': '✅',
            'in_progress': '🟡',
            'blocked': '🔴',
            'pending': '⭕'
        }.get(status, '❓')
        
        # Node shape based on type
        if node_type == 'initiative':
            return f'{node_id}["{title} {status_emoji}"]'
        elif node_type == 'project':
            return f'{node_id}["{title} {status_emoji}"]'
        else:
            return f'{node_id}["{title} {status_emoji}"]'
    
    def _edge_line(self, edge: Dict) -> str:
        """Generate line for an edge"""
        edge_type = edge['type']
        label = {
            'blocks': 'blocks',
            'enables': 'enables',
            'relates': 'relates',
            'shares': 'shares'
        }.get(edge_type, edge_type)
        
        return f'{edge["from"]} -->|{label}| {edge["to"]}'
    
    def _group_by_parent(self) -> Dict[str, List[str]]:
        """Group nodes by their parent"""
        groups = {None: []}
        
        for node_id, node in self.nodes.items():
            parent = node.get('parent')
            if parent:
                if parent not in groups:
                    groups[parent] = []
                groups[parent].append(node_id)
            else:
                groups[None].append(node_id)
        
        return groups
    
    def get_statistics(self) -> Dict:
        """Calculate graph statistics"""
        stats = {
            'total_nodes': len(self.nodes),
            'nodes_by_type': {},
            'nodes_by_status': {},
            'total_edges': len(self.edges),
            'edges_by_type': {},
            'blocking_chains': self._find_blocking_chains(),
            'orphaned_nodes': self._find_orphaned_nodes()
        }
        
        for node in self.nodes.values():
            node_type = node.get('type', 'unknown')
            status = node.get('status', 'unknown')
            
            stats['nodes_by_type'][node_type] = stats['nodes_by_type'].get(node_type, 0) + 1
            stats['nodes_by_status'][status] = stats['nodes_by_status'].get(status, 0) + 1
        
        for edge in self.edges:
            edge_type = edge.get('type', 'unknown')
            stats['edges_by_type'][edge_type] = stats['edges_by_type'].get(edge_type, 0) + 1
        
        return stats
    
    def _find_blocking_chains(self) -> List[List[str]]:
        """Find chains of blocking dependencies"""
        blocking_graph = {}
        for edge in self.edges:
            if edge['type'] == 'blocks':
                if edge['from'] not in blocking_graph:
                    blocking_graph[edge['from']] = []
                blocking_graph[edge['from']].append(edge['to'])
        
        chains = []
        visited = set()
        
        def dfs(node, path):
            if node in visited:
                return
            visited.add(node)
            path.append(node)
            
            if node in blocking_graph:
                for next_node in blocking_graph[node]:
                    dfs(next_node, path[:])
            else:
                if len(path) > 1:
                    chains.append(path)
        
        for start_node in blocking_graph:
            if start_node not in visited:
                dfs(start_node, [])
        
        return chains
    
    def _find_orphaned_nodes(self) -> List[str]:
        """Find nodes with no connections"""
        connected = set()
        for edge in self.edges:
            connected.add(edge['from'])
            connected.add(edge['to'])
        
        orphaned = []
        for node_id in self.nodes:
            if node_id not in connected:
                orphaned.append(node_id)
        
        return orphaned


def main():
    """CLI interface for graph visualizer"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Visualize Linear dependency graphs')
    parser.add_argument('graph_file', help='Path to graph.json file')
    parser.add_argument('--view', choices=['full', 'critical', 'status'], 
                       default='full', help='View type')
    parser.add_argument('--output', help='Output file path')
    parser.add_argument('--stats', action='store_true', help='Show statistics')
    
    args = parser.parse_args()
    
    visualizer = GraphVisualizer(args.graph_file)
    
    if args.stats:
        stats = visualizer.get_statistics()
        print("Graph Statistics:")
        print(json.dumps(stats, indent=2))
    else:
        mermaid = visualizer.generate_mermaid(args.view)
        
        if args.output:
            with open(args.output, 'w') as f:
                f.write(f"## Dependency Graph\n\n")
                f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                f.write("```mermaid\n")
                f.write(mermaid)
                f.write("\n```\n")
            print(f"Graph written to {args.output}")
        else:
            print(mermaid)


if __name__ == '__main__':
    main()